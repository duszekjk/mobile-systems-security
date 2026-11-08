# linevd

Źródło: `linevd.pdf`

## Strona 1

LineVD: Statement-level Vulnerability Detection using Graph
                                                                  Neural Networks
                                                                                David Hin                                                                       Andrey Kan
                                                    CREST - The Centre for Research on Engineering                                                            AWS AI Labs*
                                                     Software Technologies, University of Adelaide                                                     Adelaide, SA, Australia, 5005
                                                      Cyber Security Cooperative Research Centre                                                          avkan@amazon.com
                                                               Adelaide, Australia, 5005
                                                              david.hin@adelaide.edu.au

                                                                           Huaming Chen                                                                         M. Ali Babar




arXiv:2203.05181v2 [cs.CR] 25 Mar 2022
                                                   CREST - The Centre for Research on Engineering                                          CREST - The Centre for Research on Engineering
                                                    Software Technologies, University of Adelaide                                           Software Technologies, University of Adelaide
                                                     Cyber Security Cooperative Research Centre                                              Cyber Security Cooperative Research Centre
                                                              Adelaide, Australia, 5005                                                               Adelaide, Australia, 5005
                                                           huaming.chen@adelaide.edu.au                                                              ali.babar@adelaide.edu.au

                                         ABSTRACT                                                                                      CCS CONCEPTS
                                         Current machine-learning based software vulnerability detection                               • Security and privacy → Software security engineering.
                                         methods are primarily conducted at the function-level. However,
                                         a key limitation of these methods is that they do not indicate the                            KEYWORDS
                                         specific lines of code contributing to vulnerabilities. This limits                           Software Vulnerability Detection, Program Representation, Deep
                                         the ability of developers to efficiently inspect and interpret the                            Learning
                                         predictions from a learnt model, which is crucial for integrating
                                         machine-learning based tools into the software development work-                              ACM Reference Format:
                                         flow. Graph-based models have shown promising performance                                     David Hin, Andrey Kan, Huaming Chen, and M. Ali Babar. 2022. LineVD:
                                                                                                                                       Statement-level Vulnerability Detection using Graph Neural Networks. In
                                         in function-level vulnerability detection, but their capability for
                                                                                                                                       MSR ’22: Proceedings of the 19th International Conference on Mining Software
                                         statement-level vulnerability detection has not been extensively
                                                                                                                                       Repositories, May 23-24, 2022, Pittsburgh, PA, USA. ACM, New York, NY, USA,
                                         explored. While interpreting function-level predictions through                               12 pages. https://doi.org/10.1145/1122445.1122456
                                         explainable AI is one promising direction, we herein consider the
                                         statement-level software vulnerability detection task from a fully
                                         supervised learning perspective. We propose a novel deep learning                             1    INTRODUCTION
                                         framework, LineVD, which formulates statement-level vulnerabil-                               Identifying potential software vulnerabilities is a crucial step in
                                         ity detection as a node classification task. LineVD leverages control                         defending against cyber attacks [25]. However, it can be difficult
                                         and data dependencies between statements using graph neural net-                              and time-consuming for developers to determine which parts of
                                         works, and a transformer-based model to encode the raw source                                 the software will contribute to vulnerabilities in large software
                                         code tokens. In particular, by addressing the conflicting outputs                             systems. Consequently, interest in more accurate and efficient au-
                                         between function-level and statement-level information, LineVD                                tomated software vulnerability detection (SVD) solutions has been
                                         significantly improve the prediction performance without vulnera-                             increasing [21, 39]. Automated SVD can be broadly classified into
                                         bility status for function code. We have conducted extensive experi-                          two categories: (1) traditional methods, which can include both
                                         ments against a large-scale collection of real-world C/C++ vulnera-                           static and dynamic analysis, and (2) data-driven solutions, which
                                         bilities obtained from multiple real-world projects, and demonstrate                          leverage data mining and machine learning to predict the presence
                                         an increase of 105% in F1-score over the current state-of-the-art.                            of software vulnerabilities [22]. Traditional static tools are often
                                                                                                                                       rule-based, leveraging knowledge from security domain experts.
                                         *This work was done prior to joining Amazon.                                                  This can result in inconsistent performance due to a high number
                                                                                                                                       of false positive alerts, or completely missing more complex vul-
                                                                                                                                       nerabilities [5]. As it is challenging to define vulnerable patterns
                                         Permission to make digital or hard copies of all or part of this work for personal or
                                         classroom use is granted without fee provided that copies are not made or distributed         in an accurate and comprehensive way, data-driven solutions have
                                         for profit or commercial advantage and that copies bear this notice and the full citation     become a promising alternative.
                                         on the first page. Copyrights for components of this work owned by others than ACM               One primary reason for the increasing popularity of data-driven
                                         must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
                                         to post on servers or to redistribute to lists, requires prior specific permission and/or a   solutions can be attributed to the ever growing quantity of open-
                                         fee. Request permissions from permissions@acm.org.                                            source vulnerability data. The accumulating security vulnerabili-
                                         MSR 2022, May 23–24, 2022, Pittsburgh, PA, USA                                                ties in open-source software are regularly updated and reported to
                                         © 2022 Association for Computing Machinery.
                                         ACM ISBN 978-1-4503-XXXX-X/18/06. . . $15.00                                                  sources like the National Vulnerability Database [1]. There have
                                         https://doi.org/10.1145/1122445.1122456                                                       been many efforts that utilize the publicly available information to

## Strona 2

MSR 2022, May 23–24, 2022, Pittsburgh, PA, USA                                                     David Hin, Andrey Kan, Huaming Chen, and M. Ali Babar


                                                                            1   void common_timer_get(struct k_itimer *timr, struct itimerspec64
reduce the need for manually defining patterns and to learn from                *cur_setting)
                                                                            2   {
the data [27, 51]. As a result, data-driven solutions have generally        3     const struct k_clock *kc = timr->kclock;
shown outstanding performance in comparison to traditional static           4
                                                                            5
                                                                                  ktime_t now, remaining, iv;
                                                                                  struct timespec64 ts64;
application security testing tools [13]. One potential reason could be      6     bool sig_none;
                                                                            7
due to the learning ability of the models to incorporate latent infor-      8       sig_none = timr->it_sigev_notify == SIGEV_NONE;
                                                                            9       iv = timr->it_interval;
mation from patterns where vulnerabilities would appear in source          10
code, in addition to the underlying causes of the vulnerability.           11
                                                                           12
                                                                                    if (iv) {
                                                                                      cur_setting->it_interval = ktime_to_timespec64(iv);
    Despite the success of current data-driven approaches in the           13
                                                                           14
                                                                                    } else if (!timr->it_active) {
                                                                                      if (!sig_none)
identification of software vulnerabilities, they are often limited         15           return;
                                                                           16       }
to a coarse level of granularity. The model outputs often present          17
                                                                           18       kc->clock_get(timr->it_clock, &ts64);
developers with limited information for prediction outcome vali-           19       now = timespec64_to_ktime(ts64);
dation and interpretation, leading to extra efforts when evaluating        20
                                                                           21       if (iv && (timr->it_requeue_pending & REQUEUE_PENDING || sig_none))
and mitigating the software vulnerabilities. Consequently, many            22         timr->it_overrun += (int)kc->timer_forward(timr, now);
                                                                           23         // Added: timr->it_overrun += kc->timer_forward(timr, now);
proposed SVD solutions have transitioned to either function-level          24
                                                                           25       remaining = kc->timer_remaining(timr, now);
[9, 10, 32, 61] or slice-level [12, 33, 35, 36] predictions, which are a   26
                                                                           27       if (remaining <= 0) {
major improvement from file-level predictions [16, 24, 52]. Some           28         if (!sig_none)
other works further leverage supplementary information, such as            29
                                                                           30
                                                                                        cur_setting->it_value.tv_nsec = 1;
                                                                                    } else {
commit-level code changes with accompanying log messages, to               31         cur_setting->it_value = ktime_to_timespec64(remaining);
                                                                           32       }
build the prediction model [23, 49]. While the goal is to help practi-     33   }
tioners to prioritize the defective codes, vulnerabilities can often be
localized to a few key lines [17]. Hence, reviewing large functions        Figure 1: Vulnerable lines predicted by LineVD for a code
could still be a considerable burden. From a preliminary analysis          snippet from CVE-2018-12896, which are indicated by the
on a large C/C++ vulnerability detection dataset [19], we find that        presence of a red background. A darker red background
vulnerable functions in the dataset are on average 95 lines of code.       color indicates higher prediction confidence by LineVD.
    Fig. 1 shows an example of how statement-level SVD can be              Ground-truth vulnerable lines have red line numbers, while
beneficial. To save space, we choose a vulnerability from a smaller        dark red line numbers indicate a data or control dependency
function, which contains an integer overflow vulnerability from the        on an added line (indicated by line 23).
Linux kernel (CVE-2018-12896) that can ultimately be exploited to
cause denial-of-service. With explicit statement-level predictions,
it can be easier to interpret why the function has been predicted
as vulnerable (or alternatively, verify that the prediction was er-        challenges in SVD, we show that LineVD could provide sufficient
roneous). Focusing the developer’s attention on the highlighted            capacity to incorporate contextual information for each statement
lines can help a developer narrow down the lines needing further           in an efficient manner. The extensive evaluation of the model has
inspection based on model confidence. In this case, a statement-           been delivered in realistic scenarios; namely, heavily imbalanced
level SVD model flags the addition assignment operation on line 22,        labels and cross-project testing. In summary, this paper makes the
which contains the vulnerable integer casting operation, as most           following contributions:
suspicious, allowing a developer to more efficiently validate and
mitigate the vulnerability.                                                     • We propose a novel and efficient statement-level SVD ap-
    Refining SVD granularity towards the statement-level is still in              proach, LineVD. With the investigation of current state-of-
its infancy; latest work by Li et. al [32] has indicated the possibility          the-art interpretation-based SVD model showing declined
of leveraging the interpretable ML model, namely GNNExplainer,                    performance, LineVD achieves a significant improvement
to derive the vulnerable statements as the interpretation of learnt               for an increase of 105% in F1-score.
model. However, in our work, we find that the performance is not                • We investigate the performance effects of each stage for
sufficient and effective when classifying and ranking the latent vul-             building a GNN-based statement-level SVD model, includ-
nerable statements. Alternatively, we aim to explore the feasibility              ing the node embedding methods and GNN model selec-
and effectiveness of directly training and predicting on vulnerabili-             tion. Upon the findings, LineVD is developed to largely im-
ties at the statement level for SVD granularity refinement, which                 prove the performance via learning from the function- and
would allow data-driven solutions to directly utilize any available               statement-level information simultaneously.
statement-level information in a fully supervised manner.                       • LineVD is the first approach to jointly learn from function-
    In this paper, we propose a novel framework for statement-level               level and statement-level information via graph neural net-
SVD, namely LineVD. We focus on revisiting core components of                     works to enhance the SVD performance, which in the empiri-
data-driven SVD from the perspective of statement-level classifica-               cal evaluation has significantly outperformed the traditional
tion, which can serve as a way of allowing developers to better in-               models only using one type information.
terpret vulnerability predictions. We have explored statement-level             • We publish our dataset, source code, and models with sup-
SVD in a thorough way to find the best data-driven architecture to                porting scripts [6], which provides a ready-to-use implemen-
achieve optimal performance. With the coverage of various feature                 tation solution for future work with regards to benchmarking
extraction methods and model architectures to tackle the latent                   and comparison.

## Strona 3

LineVD: Statement-level Vulnerability Detection using Graph Neural Networks                                         MSR 2022, May 23–24, 2022, Pittsburgh, PA, USA


2     BACKGROUND                                                              reducing out-of-vocabulary issues in source code identifiers, as this
In this section, we will introduce relevant key concepts relating             approach is not reliant on pre-defined rules.
to the source code embedding and graph neural networks (GNNs),
which have played key roles for providing effective and explainable           2.2    Graph Neural Network
capabilities to SVD prediction models in recent literature works.             Recently, graph neural networks have demonstrated superior per-
                                                                              formance at mining graph data structures for social networks [7],
                                                                              spatial-temporal related traffic networks [11], and so on. For the
                                                                              downstream source code modelling tasks, transformer-based mod-
2.1     Source code embedding                                                 els have demonstrated promising results [3]. However, the complex
To tackle a language-related task with machine learning models,               syntactic and semantic characteristics, which are inherently pre-
it is necessary to transform the related textual corpora into vector          sented in the programming languages, are not explicitly leveraged.
representations. The corpora are usually specific to a given do-                 Rather than solely representing source code as a sequence of
main; e.g., one recently popular topic is source code-related tasks.          tokens, the intrinsic structure information for source code can also
The process is commonly referred to as building a language model              be effectively modelled by representing a source code snippet (or
and extracting language embeddings, which can be at the word,                 program) as a graph, G = (V, E), allowing a model to more easily
sentence, or document-level [43]. Source code modelling is the                learn latent relationships within the source code where V is the
application of language modelling to source code, which can be                set of nodes representing the program graph and E is the edge
considered a special type of structured natural language [30], and            matrix. With different types of program-related structures, the edge
has demonstrated encouraging results for a wide range of down-                matrix E denotes the corresponding syntactic and semantic infor-
stream tasks. These include code completion [41] and code clone               mation of the source code. Using this graph-based representation in
detection [57], among others [56].                                            combination with graph neural networks has resulted in improved
    For software vulnerability detection, prior approaches have uti-          performance for function-level vulnerability detection, in which a
lized document embedding methods like Doc2Vec [29], or word em-               single graph represents a single source code function (see Section
bedding methods such as GloVe [47] and Word2Vec [43] to generate              7 for further details). The program dependency graph (PDG) of a
pre-trained vectors for singular tokens, which are then aggregated            program (see Fig. 2) is an overall focus in this work, as software
in some way. For example, Cao et al. [9] utilized averaged Word2Vec           vulnerabilities often involve data and control flows [32, 48, 60].
embeddings to transform raw code statements into vector repre-
sentations.                                                                               6                    11                                   4       1

    Recently, transformer-based models have been applied to source
code modelling, allowing for large source code understanding mod-                         8          13                                             9

els to be pre-trained. They are expected to obtain higher-quality
embeddings for source code, which can be leveraged for down-                                    14                        5                    12       3
stream tasks requiring less labeled data and training resources. One
major advancement is CodeBERT [20], based on the RoBERTa [42]
                                                                                          21    15                   19       18
architecture, which was trained on six different programming lan-
guages: Python, Java, JavaScript, PHP, Ruby, and Go. Specifically,
CodeBERT was trained on 2.1 million natural language and pro-                                                        22              25

gramming language bimodal samples, and 6.4 million programming
language unimodal samples. It should be noted that CodeBERT and                                           27

Doc2Vec can produce contextual embeddings, in contrast to GloVe
and Word2Vec embeddings, which are static and hence have the                                              28                              31
same embedding for each word regardless of its context.
    Tokenization approaches for source code can vary significantly.
For word embedding-based approaches, code tokens can be split by                                                                      29


whitespace alongside punctuation, such as parenthesis and semi-
colons [35]. Alternatively, punctuation can be completely removed             Figure 2: Program Dependence Graph for Fig. 1. Black lines
[32]. In addition, code identifiers are sometimes further tokenized           represent control dependency edges; dashed red lines repre-
according to common naming conventions, such as underscores or                sent data dependency edges.
camel case. This is to help reduce the number of out-of-vocabulary
tokens, which can otherwise be significantly higher than regular
natural language due to the nature of how developers name iden-               3     THE LINEVD FRAMEWORK
tifiers. An alternative approach to manually defined tokenization             In this section, we present the LineVD framework by firstly sum-
rules is unsupervised subword tokenization. In CodeBERT, byte-                marizing the problem definition. The overall architecture is sub-
pair encoding (BPE) [54] is used to tokenize the source code tokens.          sequently discussed with details for three main components. Par-
In particular, long variable names are split into subwords based              ticularly, we demonstrate how we have incorporated the large-
on the BPE algorithm. For example, ’add_one’ may be tokenized                 scale pretrained model and developed the novel graph construction
to ’add’, ’_’, and ’one’. This is arguably a more consistent way of           method.

## Strona 4

MSR 2022, May 23–24, 2022, Pittsburgh, PA, USA                                                                            David Hin, Andrey Kan, Huaming Chen, and M. Ali Babar


                                            Feature Extraction                                                                          Classifier Learning



                                Function
       Input
      int add_one(x) {

                                                    Tokenizer     Codebert
                                                                                                                                                              ×
                                                                                                     Graph Construction                                            Vulnerable
      }
        return x + 1;                                                                                                                      ...                     Statements


                                 Statements




                                 Function          Graph Extraction          Control & Data Dependency Edges



                                                                 Figure 3: LineVD Overall Architecture


3.1     Problem Definition                                                                              LineVD takes a single function of source code as the raw input.
We formalize the identification of vulnerable statements in a func-                                 By processing and splitting the function into individual statements
tion as a binary node classification problem, i.e., learning to predict                             𝑉𝑖 , each sample is firstly tokenized via CodeBERT’s pretrained BPE
which source code statements in a function are vulnerable. Let us de-                               tokenizer. Following the collection of 𝑉 = {𝑉1, 𝑉2, ..., 𝑉𝑛 }, the entire
fine a sample of data as ((𝑉𝑖 , 𝑌𝑖 ) |𝑉𝑖 ∈ V, 𝑌𝑖 ∈ {0, 1}, 𝑖 = {1, 2, ..., 𝑛}),                     function and the individual statements comprising the function are
where V is the set of all nodes representing a statement of code in                                 passed into CodeBERT. Thus, the function-level and statement-level
the dataset and 𝑌𝑖 is the statement-level label where 1 is vulnerable                               code representation can be acquired.
and 0 is non-vulnerable. We collectively represent Y for the set of                                     Specifically, LineVD has separately embedded the function-level
labels 𝑌𝑖 . 𝑛 is the number of nodes in the dataset.                                                and statement-level codes, rather than aggregating the statement-
   For each 𝑉𝑖 , we utilize the 𝑛-hop neighborhood graph G𝑖 =                                       level embeddings for the function-level embeddings. CodeBERT
(𝑁 V𝑖 , 𝑁 E𝑖 , X𝑖 ) to encode 𝑉𝑖 with the contextual information from                               is a bimodal model, meaning it was trained on both the natural
neighboring nodes. 𝑁 V𝑖 indicates the neighborhood nodes for 𝑉𝑖 ,                                   language description of a function in addition to the function code
𝑁 E𝑖 represents the corresponding edges as an adjacency matrix,                                     itself. As input, it uses a special separator token to distinguish the
X𝑖 ∈ R𝑚×𝑑 is the node feature matrix for 𝑉𝑖 , and 𝑚 is the number of                                natural language description from the function code. While the
nodes in 𝑁 V𝑖 . The goal of LineVD is to learn a mapping 𝑓 : V → Y                                  natural language descriptions for the functions is not accessible, a
to determine the label of a given node; i.e., whether a statement                                   general operation, as specified in the literature, is applied in this
is vulnerable or not. The prediction function of LineVD, which                                      work to prepend each input with an additional separator token,
is denoted as 𝑓 , can be learned by minimizing the following loss                                   leaving the description blank. For the output of CodeBERT, we
function:                                                                                           utilize the embedding of the classification token, which is suited
                                                                                                    for code summarization tasks. This allows us to better leverage the
                                𝑛
                               ∑︁                                                                   powerful pretrained source code summarization capability of the
                         𝑚𝑖𝑛         L (𝑓 (G𝑖 , 𝑌𝑖 |𝑉𝑖 ))                               (1)         CodeBERT model.
                               𝑖=1                                                                      Overall, the feature extraction component of LineVD using Code-
where L is the cross entropy loss function.                                                         BERT produces 𝑛 + 1 feature embeddings: one embedding for the
                                                                                                    overall function, and 𝑛 embeddings for each statement, for which
3.2     Approach Overview                                                                           we denote as 𝑋 𝑣 = {𝑥 1𝑣 , 𝑥 2𝑣 , ..., 𝑥𝑛𝑣 } separately.
In this section, we present a GNN-based approach to identify the
vulnerable statements. One fundamental element is that the iden-
                                                                                                    3.2.2 Graph Construction. In LineVD, we focus on the data and
tified data and control dependencies between statements could
                                                                                                    control dependency information, for which we have introduced
sufficiently serve as the contextual information for the statement-
                                                                                                    the graph attention network (GAT) model [55]. As discussed in
level SVD task. Furthermore, we propose a novel architecture to
                                                                                                    Sec. 2.2, graph neural networks (GNNs) learn the graph structured
better leverage the semantics conveyed within the statement and
                                                                                                    data based on an information diffusion mechanism rather than
between the statements, which overall framework is illustrated
                                                                                                    squashing the information into a flat vector, which update the node
in Figure. 3. LineVD can be divided into three main components,
                                                                                                    states according to the graph connectivity to preserve the important
described in the following sections.
                                                                                                    information, i.e., the topological dependency information [53].
3.2.1 Feature Extraction. Given a snippet of source code, achieving                                    As shown in Figure. 3, a graph attention network is used to
an informative and comprehensive code representation is critical for                                construct the model for learning topological dependency informa-
subsequent model construction. LineVD is firstly designed to extract                                tion from the graph. A GAT layer will firstly take the 𝑛 output
the code features against a transformer-based method, which is                                      statement embeddings from CodeBERT along with the edges be-
considered as effective for source code related tasks with the self-                                tween each node. The graph structure, including the nodes and
supervised learning objectives.                                                                     edges information, for the function is extracted and provided to

## Strona 5

LineVD: Statement-level Vulnerability Detection using Graph Neural Networks                                      MSR 2022, May 23–24, 2022, Pittsburgh, PA, USA


GAT. Self-loops are added to include a given node within the set                    we present the dataset details for the empirical evaluation. We fur-
of its neighborhood graph. We initialize the GAT layer state vec-                   ther discuss the applied evaluation metrics, which is considered to
       (𝑙) (𝑙) (𝑙)           (𝑙)
tor {ℎ 1 , ℎ 2 , ℎ 3 , ..., ℎ𝑛 } with 𝑋 𝑣 . 𝑙 indicates the current state.          thoroughly quantify the model performance.
LineVD will propagate the information by embedding the data and
control dependent statement (i.e., the program dependence graph)
between neighboring statements in an incremental manner. There-
                                                                                    4.1    Research Questions
fore, two graph attention networks are implemented in the LineVD                    To explore statement-level vulnerability detection task and inves-
architecture. Overall, GAT is defined by its use of attention over                  tigate the performance of LineVD, we answer and motivate the
features of neighbors in its aggregation function in Eq. (2) - (5):                 following research questions:
                                                                                       RQ1: How much performance increasement can LineVD
                    (𝑙)              (𝑙)
                  𝑧𝑖      =   𝑊 (𝑙) ℎ𝑖                                        (2)   achieve in comparison with the state-of-the-art interpretati-
                                                                                    on-based SVD model? To evaluate the relative improvement of
                                        𝑇            
                   (𝑙)                         (𝑙) (𝑙)
                  𝑒𝑖,𝑗    =   LeakyReLU 𝑎®(𝑙) 𝑧𝑖 ∥𝑧 𝑗                         (3)
                                                                                    LineVD in the statement-level SVD task, we choose to compare
                                           (𝑙)
                                   exp(𝑒𝑖,𝑗 )                                       against the state-of-the-art interpretation-based model. It is con-
                    (𝑙)
                  𝛼𝑖,𝑗    =                                                   (4)   ducted from two diverse measures, which are binary classification
                                              (𝑙)
                                                                                    and ranked metrics for vulnerable statements.
                              Í
                                𝑘 ∈N (𝑖) exp(𝑒𝑖,𝑘 )
                                                                                       RQ2: How do different code embedding methods affect
             ℎ𝑖
               (𝑙+1)
                          =
                               © ∑︁ (𝑙) (𝑙) ª
                              𝜎­          𝛼𝑖,𝑗 𝑧 𝑗 ®                          (5)   statement-level vulnerability detection? Code embedding meth-
                                 𝑗 ∈N (𝑖)                                           ods have not yet been explored for statement-level SVD compared
                                                                                    to SVD at other levels of granularity.
                               «                   ¬
                                    (𝑙)
where 𝑙 is the current state, ℎ𝑖 is the node embedding vectors at                      RQ3: How do graph neural networks and function-level
current layer, 𝑊 (𝑙) is the learnable weight matrix, 𝑎® is a learnable              information contribute to LineVD performance? The effect of
weight vector, and 𝜎 is an activation function.                                     information propagation using graph neural networks on statement-
                                                                                    level SVD has yet to be explored.
3.2.3 Classifier Learning. As multi-layer perceptron (MLP) models                      RQ4: How does LineVD perform in a cross-project classifi-
are dominantly evaluated as one of the top classifiers [31, 44], we                 cation scenario? While training on a dataset containing multiple
leverage the superior learning capability of a deep neural network                  projects already reduces misrepresentation of model generalisabil-
to better train the classifier. In this work, the goal is to train a model          ity, it is still possible for samples from the same project to appear
that could jointly learn from the function-level and statement-level                in both the training and test set. Using a cross-project scenario can
code simultaneously.                                                                better represent how the model performs on a completely unseen
   To achieve this, we consider that both function-level and statement-             project, rather than only unseen samples.
level code snippet will contribute equally to the prediction out-                      RQ5: Which statement types are best distinguished by Lin-
comes. Thus, we build a shared set of linear and dropout layers                     eVD for real-world data? Investigating the model prediction out-
taking the input of function-level CodeBERT embedding and the                       comes from the perspective of statement types, particularly for
statement embeddings obtained from the GAT layer. The ReLU [45]                     real-world data, can help to understand where the model performs
function serves as the activation function. In addition, LineVD                     best and where it fails, which can guide future work and improve-
retains the consistency of the prediction outcomes from its learn-                  ments in statement-level SVD.
ing algorithm. It incorporates a element-wise multiplication be-
tween the output class of each statement and the output class of
the function-level embedding, which could be either one or zero.                    4.2    Datasets
While the vulnerable statement could be sufficient to direct the                    Recent research suggests that SVD models should be evaluated on
function to be vulnerable, we build LineVD with the element-wise                    data that could represent the distinct characteristics of real-world
multiplication to further leverage the function-level information                   vulnerabilities [10]. This means evaluating on source code extracted
for training. Moreover, this operation harmoniously balance the                     from real-world projects (i.e. non-synthetic) while maintaining an
conflicting outputs between function-level and statement-level em-                  imbalanced ratio, which is inherent for vulnerabilities in software
beddings, and will justify the decision for some scenarios, i.e., if                projects. The usage of datasets that do not satisfy these conditions
the output class of the function-level embedding is zero, then all                  would result in the inconsistency of model performance when ap-
statement-level outputs are also zero. The intuition for this is that               plied in real world scenarios. Another dataset requirement is a
a non-vulnerable function cannot have vulnerable lines. LineVD                      sufficiently large number of samples, ideally spanning multiple
outputs the predictions corresponding to the statements in the in-                  projects in order to acquire a model that can generalize well to
put function. The cross-entropy loss function is used to train the                  unseen code. The final requirement is access to ground truth labels
LineVD. More details of the implementation can be found in the                      at the statement level or traceability to the before-fix code, i.e., the
replication package [6].                                                            original git commit.
                                                                                       By extracting the code vulnerabilities from over 300 different
4    EXPERIMENTAL DESIGN AND SETUP                                                  open-source C/C++ GitHub projects, Big-Vul contains the trustwor-
In this section, we will report the experiment design details, in-                  thy source code vulnerabilities spanning 91 different vulnerability
cluding the research questions and evaluation process. Particularly,                types, which are linked to the public Common Vulnerabilities and

## Strona 6

MSR 2022, May 23–24, 2022, Pittsburgh, PA, USA                                                David Hin, Andrey Kan, Huaming Chen, and M. Ali Babar


Exposures (CVE) database [19]. A substantial amount of manual re-        at the function-level, while the test and validation set is left in the
sources has also been dedicated to ensure the quality of the dataset.    original imbalanced ratio. We choose to balance the samples at the
Meanwhile, it has provided the enriched information including            function-level as it is non-trivial to balance at the statement-level
CVE IDs, CVE severity scores and particularly the code changes,          while maintaining the contextual dependencies between statements
along with other metadata. In the end, Big-Vul provides the best fit     within a function.
for meeting the requirements to model code-centric vulnerability
detection to the best of our knowledge, containing approximately         4.3    Evaluation Metrics
10,000 vulnerable samples and 177,000 non-vulnerable samples.            We report F1 score, precision, recall, area under the receiver operat-
This large diversity in projects, rather than focusing on a limited      ing characteristic curve (ROCAUC), and area under the precision-
number of projects in particular, allows for better representation       recall curve (PRAUC). While ROCAUC is widely used to directly
of all open-source C/C++ projects (see Table 5 for the top 10 most       measure the predictive power of the model without choosing a
common projects in the dataset).                                         specific threshold, it cannot fully reflect the effectiveness when
4.2.1 Ground-truth Labels. To obtain the ground-truth labels for         dealing with imbalanced datasets. Hence, in addition to reporting
the vulnerable and non-vulnerable lines, we follow the assertions        ROCAUC for comparison with past literature, we have also used
from literature [19, 32] rather than proposing our own heuristics:       PR-AUC, which is better suited for imbalanced problems.
(1) removed lines in a vulnerability-fixing commit serve as an in-          While binary classification is the primary focus, as described in
dicator for a vulnerable line, and (2) all lines that are control or     Section 3.1, we also report ranked metrics to evaluate the perfor-
data dependent on the added lines are also treated as vulnerable.        mance of the most confident predictions of the model. The ranked
The reasoning for the second point is that any added lines in a          metrics include mean average precision (MAP), normalized dis-
vulnerability-fixing commit were added to help patch the vulnera-        counted cumulative gain (nDCG), and mean first ranking (MFR).
bility. Hence, lines that were not modified in vulnerability-fixing      Here, we define first ranking as the rank of the first correctly pre-
commit, but are related to these added lines, can be considered as       dicted vulnerable statement. We care about how well the model
related to the vulnerability.                                            performs at a certain number of 𝑘 most confident lines, as we can
   To obtain labels corresponding to lines that are dependent on         thus further limit the amount of code that needs to be reviewed by
the added lines, we first obtain the code changes from the before        the developer. In this work, we choose to use 𝑘 = 5 as an effective
and after version of the sample, where a sample in Big-Vul refers        performance representation at the top following the recommen-
to a function-level code snippet. For the before version, we remove      dation of Li et al. [32]. However, in practical usage, this threshold
all the added lines, and for the after version, we remove all the        could be adjusted by the user. Finally, we report accuracy of inter-
deleted lines. In both cases, we keep blank placeholder lines to         pretation given N nodes, where N is equal to 5 (denoted as N5 in
ensure line number consistency. The code graph extracted from            Table 1). This can be interpreted as function-level accuracy given
the after version can be used to find all lines that are control or      only the prediction results of the top five lines.
data dependent on the added lines, whose line numbers correspond            Due to the imbalanced nature of the dataset, we first find the best
to the before version. This set of lines can be combined with the        threshold for the F1-score using the validation set before calculating
set of deleted lines to obtain the final set of vulnerable lines for a   the F1-score on the test set. When determining the significance of
single sample. Commented lines are excluded in the code graph,           improvements, we use the Wilcoxon signed-rank test [59] on the
and hence are not used for training or prediction. This can be seen      F1-scores of ten runs with random seeds. The best models according
in Fig. 1 and 2; in this case, there is only a modified line, which is   to the automated hyper parameter tuning are used for the test.
treated as both a deleted line (22) and added line (23). The control
and data dependency edges in this case happen to be the same for         4.4    Hyper parameters
both the before and after version, and hence we can use Fig. 2 to        Hyper parameters of LineVD were tuned using Ray Tune [37] with
identify the lines that are control/data dependent on line 23, which     randomized grid search. The hyper parameter details can be found
are lines 3, 19, and 21.                                                 in the publicly released source code. The scores are reported cor-
                                                                         responding to the mean test results across ten runs using the best
4.2.2 Dataset Cleaning. We performed multiple filtering steps on
                                                                         hyper parameters based on the loss of the validation set.
the Big-Vul dataset. First, we remove all comments from the code.
Second, we ignore code changes that are purely cosmetic, such as
changes to whitespace, and consequently remove any functions
                                                                         4.5    Experimental Design of Research
with no non-cosmetic code changes. Third, we removed improperly                 Questions
truncated functions. A few samples in the original dataset were          4.5.1 RQ1. In RQ1, we focus on the comparison between our pro-
truncated incorrectly, resulting in an unparsable and invalid code       posed model and the existing literature methods. For SVD task, a
sample. For example, a function that was originally 50 lines may         practical experiment setting is that the vulnerability remains un-
be incorrectly truncated to 40 lines for no apparent reason. The         known for a given piece of code regardless at function level or file
reason may be due to an error in how the dataset was originally          level. Thus, leveraging the interpretable ML models for the vali-
constructed; however, there were only 30 such samples in the whole       dation and interpretation of prediction results of SVD models is
dataset. We use a random training/validation/test split ratio of         dominant. In this work, we compare LineVD with the state-of-the-
80:10:10. For the training set, we undersample the number of non-        art interpretation-based SVD model, namely IVDetect from [32].
vulnerable samples to produce an approximately balanced dataset          IVDetect is designed as an interpretable vulnerability detector which

## Strona 7

LineVD: Statement-level Vulnerability Detection using Graph Neural Networks                               MSR 2022, May 23–24, 2022, Pittsburgh, PA, USA


embeds both artificial intelligence to detect vulnerabilities and in-         this by producing multiple splits where the test set is made of a
telligence assistant to provide vulnerabilities interpretations from          single project, and the rest of the projects are used in the training
statements. It has presented the state-of-the-art performance in              and validation set. We choose the top 10 projects with the most
terms of the detection and localization capabilities with the graph-          vulnerable samples in the dataset to use as cross-project splits.
based software vulnerability detection and interpretation models.
While it has included an empirical evaluation against the existing            4.5.5 RQ5. In RQ5, we examine which statement types (e.g. if-
function-level deep learning-based approaches, a full replication of          statement, goto-statement) LineVD can correctly distinguish. We
IVDetect for comparison in RQ1 is provided in terms of the perfor-            use the node types given by Joern. For the "Control Structure" node
mance of vulnerable statements identification.                                type, we replace it with the given control structure type (e.g. if,
                                                                              while, for). For "Function Call" node types, we split them into two
4.5.2 RQ2. In RQ2, we investigate the impacts of utilizing pre-               different categories: "built-in" function calls, which are functions
trained embedding methods for statement-level vulnerability pre-              that appear in the C standard library, and "external" function calls,
diction. While vectorizing the code statement information (also               which are any other functions not found in the standard C library.
node information in this work) is a critical step, we have included           This is an important distinction, as each sample in the dataset
different feature embedding methods, including CodeBERT, Doc2Vec,             consists of a code snippet at the function-level. This means the only
and averaged GloVe embeddings to understand their impacts on                  information present in external function calls is in the identifier
prediction performance. These two baselines were chosen to repre-             name itself, along with its arguments, rather than the contents of
sent the embedding methods usually seen in vulnerability detection            the external function. For "Operator" node types, we group them
models [9, 12, 32, 35, 36]. GloVe and Word2Vec embeddings usually             into the following categories: assignment, arithmetic, comparisons,
perform similarly in the vulnerability detection context [46], and            access, and logical. Any operator node types that do not fall into
thus we only use GloVe, which was also the chosen word embedding              these categories are grouped into "other".
technique used in IVDetect [32]. For classification of the embed-
dings, we use multiple hidden layers, and freeze all parameters of            5     RESULTS
the CodeBERT model during training.
                                                                              We run our experiments on a computing cluster utilizing multiple
4.5.3 RQ3. In RQ3, we explore the effect of introducing GNN lay-              NVIDIA Tesla V100 GPUs and Xeon E5-2698v3 CPUs operating at
ers into the feature extraction component of the model. In this               2.30 GHz.
experiment, we compare the use of two popular GNN variants:
Graph Convolution Networks (GCN) [28] and Graph Attention                     5.1    RQ1: How much performance advantage
Networks (GAT) [55]. These two GNN types were chosen to ex-                          can LineVD achieve in comparison with the
plore the effect of different GNN architectures on statement-level
                                                                                     state-of-the-art SVD model?
vulnerability classification. The GNN layers are inserted after the
feature extraction component and before the final hidden layers.              Table 1 and Table 2 summarize the performance comparison of
We also test two different types of graphs extracted from the source          LineVD with respect to IVDetect, a recently proposed fine-grained
code: Program Dependence Graphs (PDG) and Control Dependence                  vulnerability detection approach, using various evaluation mea-
Graphs (CDG). PDGs consist of both data dependency edges and                  sures. We show that LineVD significantly outperforms IVDetect
control dependency edges. Data dependency edges describe how                  method in all metrics. In Table 1, the ranked metrics are included
data flows between statements in the program (which statements                to show the accuracy of different models. A higher accuracy means
are influenced by which variables), while control dependency edges            that the model can generate more precise vulnerability detection at
describe the order in which statements execute, as well as whether            the statement level. As seen in Table 1, LineVD largely outperforms
they execute or not. We use both variants to explore whether GCNs             IVDetect in all ranked metrics (𝑝 < 0.01). For ranked metrics,
and GATs can utilize data dependency information from related                 LineVD improves 𝑁 5 by 0.205 in accuracy value from 0.695 to
statements to better distinguish vulnerable statements. The control           0.900, and increases MAP@5 by 0.336 over IVDetect from 0.424 to
and data dependencies are extracted using the Joern program [60].             0.760. For MFR, LineVD improves the performance by 4.373 ranks,
We remove samples that either cannot be parsed by Joern, or are               which significantly increase the efficiency of correctly locating the
correctly parsed but do not contain control or data dependency                first vulnerable statement by 114.5%.
edges. Since the nodes produced by Joern are not necessarily at the              When examining the distribution of rankings for LineVD, we find
line-level, we group together nodes with the same line number, and            that it is extremely skewed towards the lower end, with some highly
remove nodes with no line numbers (e.g. metadata nodes).                      incorrect predictions raising the MFR. The distribution of first-rank
   In addition to the GNN component, we simultaneously explore                scores is plotted in Figure. 4, which shows that the majority (89%)
how to incorporate the function-level information, for which it may           of first ranking scores are between 1 to 5. This suggests that LineVD
benefit LineVD to reduce the false positive rate of statement-level           may struggle with certain types of longer functions, but correctly
classification. This is done through training on the function-level           ranks them in most cases.
label of the function, which is embedded using CodeBERT.                         Table 2 provides the binary classification metrics, which is the
                                                                              most straightforward evaluation (whether or not a line is correctly
4.5.4 RQ4. In RQ4, we explore how LineVD performs in a cross-                 predicted as vulnerable statement), and the one directly aligned
project scenario; i.e. samples from the target project do not appear          with our problem definition. Overall, LineVD outperforms IVDetect
in the source projects which are used in model training. We simulate          by 104% (𝑝 < 0.01) in F1-score. Specifically, for practical usage, we

## Strona 8

MSR 2022, May 23–24, 2022, Pittsburgh, PA, USA                                               David Hin, Andrey Kan, Huaming Chen, and M. Ali Babar


 600                                                                    for statement-level information. In Table 3, CodeBERT has out-
                                          50
 500                                                                    performed the baseline feature embedding methods, which are
                                          40                            Doc2Vec and GloVe, in the context of statement-level vulnerability
 400                                                                    prediction. CodeBERT increases the value of F1-score in compari-
                                          30                            son to Doc2Vec by 134% (𝑝 < 0.01), and GloVe by 16% (𝑝 < 0.05)
 300
                                                                        respectively. This is to be expected, as the pre-trained CodeBERT
 200                                      20
                                                                        model is designed with over 125 million parameters, which provide
 100                                      10                            an enhanced capability to encode richer information in a larger and
                                                                        deeper model from code snippets comparing to the other models
   0                                      0                             with less layers and parameters.
       1      2        3     4      5       0            50    100
                                   First Ranking                           We also note that, while CodeBERT has the advantage over GloVe
                                                                        and Doc2Vec being pre-trained on a large corpus, it has the disad-
                                                                        vantage of being trained on an external dataset consisting of non
Figure 4: Histogram of first rankings of LineVD on default
                                                                        C/C++ code in five other programming languages. In comparison,
test set. First ranking is defined as the first true-positive
                                                                        the GloVe and Doc2Vec models are directly trained on our C/C++
statement in a sorted list of softmax scores assigned to each
                                                                        dataset. Since Doc2Vec should be able to provide a better encoding
statement for a given function. E.g. in 575 samples, a vulner-
                                                                        capability for the contextual information about statements, GloVe
able statement is first in the ranked list of vulnerable state-
                                                                        presents a second best performance by the averaged aggregation
ment predictions; in 67 samples, a vulnerable statement is
                                                                        method. Nonetheless, CodeBERT provides a best code embedding
second in the list, etc.
                                                                        method given the comparative experiments with the other most
                                                                        popular code embedding methods for SVD to date.
notice that recall score has also been substantially improved from
0.140 to 0.533, indicating that LineVD has boosted the ability to       Table 3: RQ2: Feature Embedding Methods for Statement-
correctly determine and locate the vulnerable statements.               level Vulnerability Classification
    We also note that another advantage of our architecture regards
its efficiency in generating statement-level predictions compared to     Embedding      F1         Rec         Prec        ROCAUC PRAUC
IVDetect. The use of an explanation model significantly increases
the inference time for a single sample, as an entire model must          Doc2Vec        0.064      0.167       0.040       0.580       0.508
be trained to find a subgraph that explains the model’s prediction,      GloVe          0.129      0.166       0.106       0.666       0.529
compared to the single forward pass required by LineVD. Using an         CodeBERT       0.150      0.254       0.121       0.703       0.534
NVIDIA Tesla V100, a single inference using GNNExplainer can
take over a minute, depending on its configuration, while the single
forward pass in LineVD takes less than a second.                        5.3    RQ3: Can graph neural networks and
                                                                               function-level information benefit
5.2     RQ2: How do different code embedding                                   statement-level classification?
        methods affect statement-level
                                                                        Table. 4 shows the effect of different experiment settings involving
        vulnerability detection?                                        GNN type, program graph type, and whether or not the function-
We evaluate the effectiveness of CodeBERT regarding the code            level classification component is included in the model. As it could
embedding methods. To be able to justify and simplify the compar-       be seen from Table. 4, using graph attention network for the feature
ison with same process, as stated in section. 4.5.2, the multi-layer    learning from PDG information is the best fit, which we have hence
perceptron model is chosen and we limit the embedding process           included as the graph component in LineVD. When comparing
                                                                        this GNN feature extraction combination with the model variation
    Table 1: RQ1: Statement-level Performance (Ranked)                  without GNN, we achieve an increase of 24% in F1 score (𝑝 < 0.01)
                                                                        from 0.296 to 0.360, indicating that the presence of the GNN benefits
                                                                        the model’s learning capability. However, the performance of other
 Methods          N5             MAP@5           NDCG@5       MFR       graph-based combinations is generally comparable to using the
 IVDetect         0.695          0.424           0.517        8.192     model without a GNN. This suggests that the program graph type
 LineVD           0.900          0.760           0.804        3.819     and GNN type non-trivially affects the performance of the model. In
                                                                        particular, only using control dependency edges generally results in
                                                                        lower performance than using both control and data dependencies,
Table 2: RQ1: Statement-level Performance (classification)              suggesting that data dependency edges are important in predicting
                                                                        statement-level vulnerabilities.
 Methods          F1       Rec           Prec      ROCAUC       PRAUC      In addition, we find that GCN achieves worse performance in
                                                                        comparison to GAT for all model types, which is to be expected, as
 IVDetect         0.176    0.140         0.238     0.463        0.520
                                                                        the feature aggregation in GCN treats all neighboring nodes equally,
 LineVD           0.360    0.533         0.271     0.913        0.642
                                                                        unlike GAT, which attends to certain neighbors. However, when

## Strona 9

LineVD: Statement-level Vulnerability Detection using Graph Neural Networks                                  MSR 2022, May 23–24, 2022, Pittsburgh, PA, USA


comparing only using statement-level information for classification                Table 5: RQ4: Cross-project Statement-level Prediction
(i.e. no function-level information involved), the use of GCN with
either of the graph types or a GAT with CDG results in worse                      Project          F1      Rec      Prec     ROCAUC        PRAUC        Vuln
performance compared to using no GNN. Finally, we find that the
                                                                                  Chromium         0.298   0.470    0.219    0.923         0.625        3103
enrichment of function-level information in the model significantly
                                                                                  Linux            0.301   0.502    0.216    0.925         0.630        1847
increases the statement-level performance, regardless of whether
                                                                                  Android          0.290   0.494    0.208    0.922         0.625        962
a GNN is used. Using the GAT+PDG combination, we achieve a
                                                                                  ImageMagick      0.333   0.504    0.249    0.925         0.644        331
performance increase of 140% (𝑝 < 0.01).
                                                                                  PHP              0.290   0.487    0.208    0.928         0.622        200
                                                                                  TCPDump          0.284   0.452    0.207    0.925         0.622        197
Table 4: RQ3: Graph-based Feature Variants for Statement-                         OpenSSL          0.298   0.508    0.211    0.926         0.628        157
level Vulnerability Classification                                                Krb5             0.259   0.535    0.186    0.903         0.605        139
                                                                                  QEMU             0.250   0.478    0.177    0.910         0.601        120
 Model Type                 F1        Rec      Prec      ROCAUC         PRAUC     FFmpeg           0.269   0.483    0.193    0.917         0.612        115
 GAT+CDG                  0.115      0.120     0.112       0.657         0.528
 GAT+CDG+Func             0.304      0.491     0.221       0.907         0.624      Table 6: RQ5: Analysis of Statement-level Predictions
 GAT+PDG                  0.150      0.254     0.121       0.703         0.534
 GAT+PDG+Func             0.360      0.533     0.271       0.913         0.642
 GCN+CDG                  0.084      0.143     0.060       0.632         0.514    Statement Type             TP       FP       TN        FN        F1
 GCN+CDG+Func             0.283      0.558     0.190       0.911         0.597    Function Declaration       530      364      17572     126       0.68
 GCN+PDG                  0.085      0.125     0.067       0.599         0.513    While Statement            48       72       1374      23        0.50
 GCN+PDG+Func             0.310      0.460     0.235       0.905         0.616    Builtin Function Call      142      246      4537      72        0.47
 No GNN                   0.129      0.166     0.106       0.666         0.529    Logical Operation          90       159      4601      60        0.45
 No GNN+Func              0.296      0.537     0.205       0.921         0.619    Switch Statement           18       31       1424      31        0.37
                                                                                  For Statement              75       195      3632      88        0.35
                                                                                  If Statement               749      1930     50969     855       0.35
                                                                                  Assignment Operation       1206     3792     81490     1051      0.33
5.4     RQ4: How does LineVD perform in a                                         Other Operation            62       200      5401      54        0.33
        cross-project classification scenario?                                    Jump Target                18       53       11119     19        0.33
From Table 5, we can see that performance is generally consistent                 Arithmetic Operation       27       106      1379      10        0.32
throughout the different projects. Due to the nature of the vari-                 Return Statement           166      526      27332     186       0.32
ous projects, there are varying numbers of vulnerable samples for                 External Function Call     644      2212     63378     582       0.32
each project. The top 10 software projects are reported in Table                  Comparison Operation       19       64       1489      17        0.32
5. While the performance varies, in general, they are all slightly                Access Operation           44       168      3488      48        0.29
lower than the results from the random splits in Table 2. This is par             Cast Operation             25       115      3146      28        0.26
for the course, as even partial inclusion of within-project informa-              Continue                   2        13       1039      1         0.22
tion such as variable and function names may assist the model in                  Break                      5        42       7966      43        0.11
distinguishing vulnerable samples.                                                Goto Statement             3        15       5115      48        0.09
   In Table 5, the investigated projects are ranked according to the
number of vulnerabilities, which is indicated in the last column
‘Vuln’. We note that the Chromium and Linux splits contain a dispro-
                                                                                 the significantly higher level of information in function declara-
portionately large number of vulnerable samples. The Chromium
                                                                                 tions compared to other statements, which can consist of the return
split itself accounts for 30% of all vulnerable samples in the dataset.
                                                                                 type, function name, parameter types, and the parameter names.
Despite this, the performance is competitive with the other splits,
                                                                                 Operation-related statements generally perform similarly, except
indicating that the model attains a high generalisability for different
                                                                                 for logical operations, which LineVD can generally better distin-
settings, which has shown comparable performance with a smaller
                                                                                 guish, and access and cast operations, which are achieve relatively
training set in Table 5.
                                                                                 poorer performance.
                                                                                    LineVD has higher performance with built-in function call state-
5.5     RQ5: Which statement types are best                                      ments compared to external function calls. This is somewhat ex-
        distinguished by LineVD?                                                 pected, as the same built-in functions are likely to appear across
Table 6 shows the raw prediction results for different statement                 more samples, unlike user-defined function names. In addition, due
types. We report the confusion matrix values for each statement                  to the function-level nature of the dataset, the only information
type and sort them by F1 score. We see that that assignment op-                  in external function call statements is from the function name it-
erations and external function calls are the most commonly oc-                   self and the arguments passed. Without knowledge of what occurs
curring vulnerable lines, and that the model most often correctly                within an external function call, it can be difficult to find distin-
classifies Function Declaration statements. This could be due to                 guishing patterns relating to their vulnerability.

## Strona 10

MSR 2022, May 23–24, 2022, Pittsburgh, PA, USA                                                David Hin, Andrey Kan, Huaming Chen, and M. Ali Babar


   LineVD struggles most with continue, break, and goto state-           across the different baseline models. However, this is something
ments. These are all control structure nodes that affect the control     that could be tested more thoroughly in future works.
dependency graph, and do not contain any direct statement-level
information that could distinguish them from each other. Hence, to       6.2    Limitations and Future Work
distinguish the vulnerability of these statements, the model must        While LineVD outperforms the current state-of-the-art, the per-
rely on the patterns relating to the context in which they appear.       formance is still quite low, meaning there is still much room for
Despite using a GNN to capture these relationships, these state-         improvement in the statement-level SVD task. A particular area of
ments still cannot be classified correctly. Hence, while the use of      interest is finding the best way to produce better code embeddings.
GNN does improve overall performance, these results indicate that        While CodeBERT can perform well, it is not trained on C/C++.
neither GCN or GAT are sufficient for effectively distinguishing         The use of a large language model pretrained on the specific tar-
these particular control statements. In contrast, statement types        get language (e.g. C-BERT [8]) could improve the performance of
like function declarations, function calls, and for/while/if control     downstream tasks. However, at the time of writing, there were no
structures often contain significantly more information within the       openly released C/C++-based large pretrained models.
statement, and hence can be distinguished more easily. This focus            Another limitation regards the learning capability of the GNN
on more complex control structure statement types and built-in           layer, which inherently only propagates information from imme-
function calls is suitable for practical usage as they are more likely   diately neighboring nodes (i.e. 1-hop). To propagate further range
to be directly involved in the vulnerability.                            information, multiple graph neural network layers can be stacked.
                                                                         For example, two GNN layers would propagate information across
6     DISCUSSION                                                         a 2-hop neighborhood for each node. However, most graph neural
In this section, we discuss the threats to validity and limitations of   network architectures using more than just a few layers has been
our work, along with ideas for future work.                              shown to result in over-squashing, where the exponentially grow-
                                                                         ing information between each layer cannot be captured within a
                                                                         fixed-length vector [4], resulting in bottlenecked performance. This
6.1     Threats to Validity
                                                                         is consistent with our findings; we tuned the number GNN layers
The first threat relates to the potential sub-optimal hyper param-       during experimentation but did not find any significant increase in
eter tuning; we rely on a random grid search for determining the         performance beyond two layers.
combinations of hyper parameters; however, it would be close to              Future work could explore novel GNN architectures that can
impossible to exhaustively test all combinations of hyper parame-        better capture vulnerability patterns in program graphs. Moreover,
ters. To mitigate this threat, we adopt best practices where possible    it is recognized that, amid the two different categories of software
when choosing the default range of values for the hyper parameter        metrics-based [16, 24, 52] and pattern-based [33, 34, 36] approaches
search, and tune each model variation with the same number of            as data-driven SVD solutions, a few of them could have the potential
random parameter configurations.                                         of delivering a fine-grained prediction outcome. In the future work,
   Another threat is about the dataset. We use a maintained C/C++        the investigation of a systematic comparison with other tools would
dataset built for vulnerability detection as the same usage as in        give broader and deeper perspective of evaluation.
[32]. Thus, it has appeared that the information from the dataset
generally target on intral-procedural information. Most samples
                                                                         7     RELATED WORK
in current vulnerability detection datasets [10, 19, 61] lack inter-
procedural information (including functions from other files), which     To recap the state-of-the-art of software vulnerability detection
make it difficult for both learning-based approaches and regular         researches, we introduce the related work from two perspectives:
static analysis tools to determine the underlying nature of a vulner-    1) the application of GNN on SVD, 2) the explanability of machine
ability. Certain requirements would be necessary, such as handling       learning models for SVD.
macros and inter-procedural function calls, to capture all necessary
information to learn the underlying nature of the vulnerabilities.       7.1    Software vulnerability detection with GNN
These requirements are non-trivial such that training a learning-        Detecting software vulnerability is an ongoing topic to secure soft-
based model is an extremely challenging task if only looking at          ware systems from cyber attacks. Recent advances have advocated
source code. However, future works could explore the possibility of      the application of GNN and its variants for function level vulnerabil-
producing datasets with deeper contextual information for individ-       ity detections, which is considered as the best way of representing
ual samples, which could then be used to more comprehensively            source code in the SVD context [2, 61], and have demonstrated
test the capabilities of GNNs for solving these issues.                  enhanced performance over other approaches [9, 17, 32].
   There has also been recent work on the effect of time-based              The introduction of GNNs for modelling vulnerabilities was orig-
validation on software defect prediction [18], which could also          inally inspired by the vulnerability discovery approach proposed
be relevant to vulnerability detection. We mitigate this threat by       by Yamaguchi et al. [60] using Code Property Graphs, a type of
also exploring cross-project vulnerability prediction, since time-       program graph incorporating program dependency edges [26, 40],
based validation primarily applies to within-project prediction. Fur-    control flow edges, and the abstract syntax tree of the program,
thermore, any graph-based model should intuitively have similar          which provide an additional source of information to learn from
capabilities in regards to learning patterns associated with vulnera-    [14]. Hence, the performance improvements using GNNs can pri-
bilities, and hence the performance loss (or gain) should be linear      marily be attributed to leveraging the domain knowledge that lines

## Strona 11

LineVD: Statement-level Vulnerability Detection using Graph Neural Networks                                       MSR 2022, May 23–24, 2022, Pittsburgh, PA, USA


of source code within a program have specific relationships to other          utilizing statement-level information for statement-level SVD. Fi-
lines; i.e., training using both semantic and syntactical information,        nally, LineVD achieves reasonable cross-project performance, in-
rather than only syntactical information.                                     dicating its effectiveness and generalization capabilities even for
   To achieve this goal, the lines of source code, which is also the          completely unseen software projects. Future directions will include
nodes in the graph, will be firstly vectorized according to the possi-        exploring alternate pretrained feature embedding methods and
ble code tokens. The vectorized information is then concatenated              novel GNN architectures that can better accommodate the underly-
as initial node information to allow GNNs to capture the seman-               ing nature of software source code and the vulnerabilities.
tic and syntactical information. This propagation of information
between semantically relevant statements theoretically allows the
model to better make use of relevant contextual lines. While GNNs             ACKNOWLEDGMENT
have been shown to perform well in function-level vulnerability               The work was supported by the Cyber Security Research Centre
classification (graph classification) [9, 10, 12, 38, 61], the effects of     Limited whose activities are partially funded by the Australian Gov-
vectorized methods and GNNs models on statement-level vulnera-                ernment’s Cooperative Research Centres Programme. This work
bility classification (node classification) have yet to be explored.          was supported with supercomputing resources provided by the
                                                                              Phoenix HPC service at the University of Adelaide.

7.2     Interpretation machine-learning based                                 REFERENCES
        models for SVD                                                         [1] 2021. NIST: National Vulnerability Database. https://nvd.nist.gov/.
                                                                               [2] Wasi Uddin Ahmad, Saikat Chakraborty, Baishakhi Ray, and Kai-Wei Chang.
One way to improve the performance of machine-learning based                       2021. Unified Pre-training for Program Understanding and Generation. In Pro-
method for SVD in practice is the development of explainable de-                   ceedings of the 2021 Conference of the North American Chapter of the Association
tection results, which could provide a fine-grained vulnerability                  for Computational Linguistics: Human Language Technologies. Association for
                                                                                   Computational Linguistics, 2655–2668.
prediction outcome. Particularly, there have been works attempt-               [3] Miltiadis Allamanis, Marc Brockschmidt, and Mahmoud Khademi. 2018. Learning
ing to detecting lines-level information by leveraging explainable                 to Represent Programs with Graphs. In International Conference on Learning
                                                                                   Representations. 1–17.
artificial intelligence for software engineering tasks, such as detect-
                                                                               [4] Uri Alon and Eran Yahav. 2020. On the bottleneck of graph neural networks and
ing source code lines for defect prediction [50, 58]. This raises the              its practical implications. In International Conference on Learning Representations
importance of research for interpretable machine-learning based                    (ICLR). 1–16.
                                                                               [5] Bushra Aloraini, Meiyappan Nagappan, Daniel M German, Shinpei Hayashi,
models. Besides the novel machine-learning based model for func-                   and Yoshiki Higo. 2019. An empirical study of security warnings from static
tion level vulnerability detection output, the existing works are                  application security testing tools. Journal of Systems and Software 158 (2019),
limited to providing partial information for the explanation gener-                110427.
                                                                               [6] Authors. 2022. Reproduction package for MSR double-blind review. Retrieved
ation, i.e., tokens from [62] and intermediate code by [33]. Other                 Jan, 2022 from. https://github.com/davidhin/linevd
way for statement-level SVD task may be via localizing the specific            [7] Ranran Bian, Yun Sing Koh, Gillian Dobbie, and Anna Divoli. 2019. Network
                                                                                   embedding and change modeling in dynamic heterogeneous networks. In Proceed-
vulnerable statements with the assumption of receiving vulnera-                    ings of the 42nd International ACM SIGIR Conference on Research and Development
ble source codes in function level [15]. However, it demonstrates                  in Information Retrieval. 861–864.
a certain limitation as SV detection and localization are mostly               [8] Luca Buratti, Saurabh Pujar, Mihaela Bornea, Scott McCarley, Yunhui Zheng,
                                                                                   Gaetano Rossiello, Alessandro Morari, Jim Laredo, Veronika Thost, Yufan Zhuang,
demanded at the same time.                                                         et al. 2020. Exploring software naturalness through neural language models.
   A recently explored benefit of GNNs for SVD is direct access                    arXiv preprint arXiv:2006.12641 (2020).
to explainable GNN approaches [32]. These can be attached to                   [9] Sicong Cao, Xiaobing Sun, Lili Bo, Ying Wei, and Bin Li. 2021. BGNN4VD:
                                                                                   Constructing Bidirectional Graph Neural-Network for Vulnerability Detection.
any GNN-based function-level SVD model to obtain fine-grained                      Information and Software Technology 136 (2021), 106576.
predictions; i.e., statement-level predictions if the nodes themselves        [10] Saikat Chakraborty, Rahul Krishna, Yangruibo Ding, and Baishakhi Ray. 2021.
                                                                                   Deep learning based vulnerability detection: Are we there yet. IEEE Transactions
represent statements. However, whether or not it is the best way to                on Software Engineering (2021).
build a statement-level vulnerability classifier has yet to be explored.      [11] Cen Chen, Kenli Li, Sin G Teo, Xiaofeng Zou, Kang Wang, Jie Wang, and Zeng
For example, one disadvantage of using a function-level detector as                Zeng. 2019. Gated residual recurrent graph neural networks for traffic prediction.
                                                                                   In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 33. 485–492.
the base model for interpretation is the inability to directly leverage       [12] Xiao Cheng, Haoyu Wang, Jiayi Hua, Guoai Xu, and Yulei Sui. 2021. DeepWukong:
any statement-level information during the training process, in                    Statically detecting software vulnerabilities using deep graph neural network.
addition to the significantly longer inference times.                              ACM Transactions on Software Engineering and Methodology (TOSEM) 30, 3 (2021),
                                                                                   1–33.
                                                                              [13] Roland Croft, Dominic Newlands, Ziyu Chen, and M Ali Babar. 2021. An Empirical
                                                                                   Study of Rule-Based and Learning-Based Approaches for Static Application
                                                                                   Security Testing. In Proceedings of the 15th ACM/IEEE International Symposium
8     CONCLUSION                                                                   on Empirical Software Engineering and Measurement (ESEM). 1–12.
We introduce LineVD, a novel deep learning approach for statement-            [14] Lei Cui, Zhiyu Hao, Yang Jiao, Haiqiang Fei, and Xiaochun Yun. 2020. VulDetector:
                                                                                   Detecting Vulnerabilities Using Weighted Feature Graph Comparison. IEEE
level vulnerability detection, which can allow developers to more ef-              Transactions on Information Forensics and Security 16 (2020), 2004–2017.
ficiently evaluate potentially vulnerable functions. LineVD achieves          [15] Yangruibo Ding, Sahil Suneja, Yunhui Zheng, Jim Laredo, Alessandro Morari, Gail
                                                                                   Kaiser, and Baishakhi Ray. 2022. VELVET: a noVel Ensemble Learning approach to
a new state-of-the-art on statement-level vulnerability detection                  automatically locate VulnErable sTatements. In 2022 IEEE International Conference
on real-world open source projects by leveraging graph neural                      on Software Analysis, Evolution and Reengineering (SANER). IEEE, 1–12.
networks and statement-level information during training. The                 [16] Xiaoning Du, Bihuan Chen, Yuekang Li, Jianmin Guo, Yaqin Zhou, Yang Liu, and
                                                                                   Yu Jiang. 2019. Leopard: Identifying vulnerable code for vulnerability assessment
significant improvement in comparison to the latest fine-grained                   through program metrics. In 2019 IEEE/ACM 41st International Conference on
machine-learning based model indicates the effectiveness of directly               Software Engineering (ICSE). IEEE, 60–71.

## Strona 12

MSR 2022, May 23–24, 2022, Pittsburgh, PA, USA                                                                           David Hin, Andrey Kan, Huaming Chen, and M. Ali Babar


[17] Xu Duan, Jingzheng Wu, Shouling Ji, Zhiqing Rui, Tianyue Luo, Mutian Yang,                    Multimedia Information Networking and Security. IEEE, 152–156.
     and Yanjun Wu. 2019. VulSniper: Focus Your Attention to Shoot Fine-Grained               [40] Chao Liu, Chen Chen, Jiawei Han, and Philip S Yu. 2006. GPLAG: detection of
     Vulnerabilities.. In Proceedings of the 27th International Conference on International        software plagiarism by program dependence graph analysis. In Proceedings of
     Joint Conferences on Artificial Intelligence. 4665–4671.                                      the 12th ACM SIGKDD international conference on Knowledge discovery and data
[18] Davide Falessi, Jacky Huang, Likhita Narayana, Jennifer Fong Thai, and Burak                  mining. 872–881.
     Turhan. 2020. On the need of preserving order of data when validating within-            [41] Fang Liu, Ge Li, Yunfei Zhao, and Zhi Jin. 2020. Multi-task learning based pre-
     project defect classifiers. Empirical Software Engineering 25, 6 (2020), 4805–4830.           trained language model for code completion. In Proceedings of the 35th IEEE/ACM
[19] Jiahao Fan, Yi Li, Shaohua Wang, and Tien N Nguyen. 2020. AC/C++ Code                         International Conference on Automated Software Engineering. 473–485.
     Vulnerability Dataset with Code Changes and CVE Summaries. In Proceedings of             [42] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer
     the 17th International Conference on Mining Software Repositories. 508–512.                   Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. Roberta: A
[20] Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong,                      robustly optimized bert pretraining approach. arXiv preprint arXiv:1907.11692
     Linjun Shou, Bing Qin, Ting Liu, Daxin Jiang, et al. 2020. CodeBERT: A Pre-                   (2019).
     Trained Model for Programming and Natural Languages. In Findings of the Asso-            [43] Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Corrado, and Jeff Dean. 2013.
     ciation for Computational Linguistics: EMNLP 2020. 1536–1547.                                 Distributed representations of words and phrases and their compositionality. In
[21] Seyed Mohammad Ghaffarian and Hamid Reza Shahriari. 2017. Software vulnera-                   Advances in Neural Information Processing Systems. 3111–3119.
     bility analysis and discovery using machine-learning and data-mining techniques:         [44] Hajra Naeem and Manar H Alalfi. 2020. Identifying Vulnerable IoT Applications
     A survey. ACM Computing Surveys (CSUR) 50, 4 (2017), 1–36.                                    using Deep Learning. In 2020 IEEE 27th International Conference on Software
[22] Hazim Hanif, Mohd Hairul Nizam Md Nasir, Mohd Faizal Ab Razak, Ahmad Fir-                     Analysis, Evolution and Reengineering (SANER). IEEE, 582–586.
     daus, and Nor Badrul Anuar. 2021. The rise of software vulnerability: Taxonomy           [45] Vinod Nair and Geoffrey E Hinton. 2010. Rectified linear units improve re-
     of software vulnerabilities detection and machine learning approaches. Journal                stricted boltzmann machines. In Proceedings of the 27th International Conference
     of Network and Computer Applications (2021), 103009.                                          on International Conference on Machine Learning. 807–814.
[23] Thong Hoang, Hong Jin Kang, David Lo, and Julia Lawall. 2020. Cc2vec: Dis-               [46] Hai Ngoc Nguyen, Songpon Teerakanok, Atsuo Inomata, and Tetsutaro Uehara.
     tributed representations of code changes. In Proceedings of the ACM/IEEE 42nd                 2021. The Comparison of Word Embedding Techniques in RNNs for Vulnerability
     International Conference on Software Engineering. 518–529.                                    Detection.. In ICISSP. 109–120.
[24] Aram Hovsepyan, Riccardo Scandariato, and Wouter Joosen. 2016. Is Newer                  [47] Jeffrey Pennington, Richard Socher, and Christopher D Manning. 2014. Glove:
     Always Better? The Case of Vulnerability Prediction Models. In Proceedings of                 Global vectors for word representation. In Proceedings of the 2014 Conference on
     the 10th ACM/IEEE International Symposium on Empirical Software Engineering                   Empirical Methods in Natural Language Processing (EMNLP). 1532–1543.
     and Measurement. 1–6.                                                                    [48] Nam H Pham, Tung Thanh Nguyen, Hoan Anh Nguyen, and Tien N Nguyen. 2010.
[25] Julian Jang-Jaccard and Surya Nepal. 2014. A survey of emerging threats in                    Detection of recurring software vulnerabilities. In Proceedings of the IEEE/ACM
     cybersecurity. J. Comput. System Sci. 80, 5 (2014), 973–993.                                  international conference on Automated software engineering. 447–456.
[26] Andrew Johnson, Lucas Waye, Scott Moore, and Stephen Chong. 2015. Explor-                [49] Chanathip Pornprasit and Chakkrit Tantithamthavorn. 2021. JITLine: A Simpler,
     ing and enforcing security guarantees via program dependence graphs. ACM                      Better, Faster, Finer-grained Just-In-Time Defect Prediction. In 2021 International
     SIGPLAN Notices 50, 6 (2015), 291–302.                                                        Conference on Mining Software Repositories (MSR’21). 1–11.
[27] Seulbae Kim, Seunghoon Woo, Heejo Lee, and Hakjoo Oh. 2017. Vuddy: A                     [50] Chanathip Pornprasit and Chakkrit Tantithamthavorn. 2022. DeepLineDP: To-
     scalable approach for vulnerable code clone discovery. In 2017 IEEE Symposium                 wards a Deep Learning Approach for Line-Level Defect Prediction. IEEE Trans-
     on Security and Privacy (SP). IEEE, 595–614.                                                  actions on Software Engineering 01 (2022), 1–1.
[28] Thomas N. Kipf and Max Welling. 2017. Semi-Supervised Classification with                [51] Hitesh Sajnani, Vaibhav Saini, Jeffrey Svajlenko, Chanchal K Roy, and Cristina V
     Graph Convolutional Networks. In Proceedings of the 5th International Conference              Lopes. 2016. Sourcerercc: Scaling code clone detection to big-code. In Proceedings
     on Learning Representations (Palais des Congrès Neptune, Toulon, France) (ICLR                of the 38th International Conference on Software Engineering. 1157–1168.
     ’17).                                                                                    [52] Riccardo Scandariato, James Walden, Aram Hovsepyan, and Wouter Joosen. 2014.
[29] Quoc Le and Tomas Mikolov. 2014. Distributed representations of sentences and                 Predicting vulnerable software components via text mining. IEEE Transactions
     documents. In International Conference on Machine Learning. PMLR, 1188–1196.                  on Software Engineering 40, 10 (2014), 993–1006.
[30] Triet HM Le, Hao Chen, and Muhammad Ali Babar. 2020. Deep learning for                   [53] Franco Scarselli, Marco Gori, Ah Chung Tsoi, Markus Hagenbuchner, and Gabriele
     source code modeling and generation: Models, applications, and challenges. ACM                Monfardini. 2008. The graph neural network model. IEEE transactions on neural
     Computing Surveys (CSUR) 53, 3 (2020), 1–38.                                                  networks 20, 1 (2008), 61–80.
[31] Stefan Lessmann, Bart Baesens, Christophe Mues, and Swantje Pietsch. 2008.               [54] Rico Sennrich, Barry Haddow, and Alexandra Birch. 2016. Neural Machine
     Benchmarking classification models for software defect prediction: A proposed                 Translation of Rare Words with Subword Units. (2016), 1715–1725.
     framework and novel findings. IEEE Transactions on Software Engineering 34, 4            [55] Petar Veličković, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro
     (2008), 485–496.                                                                              Liò, and Yoshua Bengio. 2018. Graph Attention Networks. In Proceedings of the
[32] Yi Li, Shaohua Wang, and Tien N Nguyen. 2021. Vulnerability Detection with Fine-              6th International Conference on Learning Representations. 1–12.
     grained Interpretations. In The 29th ACM Joint European Software Engineering             [56] Deze Wang, Yue Yu, Shanshan Li, Wei Dong, Ji Wang, and Liao Qing. 2021. Mul-
     Conference and Symposium on the Foundations of Software Engineering. ACM.                     Code: A Multi-task Learning Approach for Source Code Understanding. In 2021
[33] Zhen Li, Deqing Zou, Shouhuai Xu, Zhaoxuan Chen, Yawei Zhu, and Hai Jin.                      IEEE International Conference on Software Analysis, Evolution and Reengineering
     2021. Vuldeelocator: a deep learning-based fine-grained vulnerability detector.               (SANER). IEEE, 48–59.
     IEEE Transactions on Dependable and Secure Computing (2021), 1–17.                       [57] Wenhan Wang, Ge Li, Bo Ma, Xin Xia, and Zhi Jin. 2020. Detecting code clones
[34] Zhen Li, Deqing Zou, Shouhuai Xu, Hai Jin, Hanchao Qi, and Jie Hu. 2016.                      with graph neural network and flow-augmented abstract syntax tree. In 2020 IEEE
     Vulpecker: an automated vulnerability detection system based on code similarity               27th International Conference on Software Analysis, Evolution and Reengineering
     analysis. In Proceedings of the 32nd Annual Conference on Computer Security                   (SANER). IEEE, 261–271.
     Applications. 201–213.                                                                   [58] Supatsara Wattanakriengkrai, Patanamon Thongtanunam, Chakkrit Tan-
[35] Zhen Li, Deqing Zou, Shouhuai Xu, Hai Jin, Yawei Zhu, and Zhaoxuan Chen. 2021.                tithamthavorn, Hideaki Hata, and Kenichi Matsumoto. 2020. Predicting De-
     SySeVR: A framework for using deep learning to detect software vulnerabilities.               fective Lines Using a Model-Agnostic Technique. IEEE Transactions on Software
     IEEE Transactions on Dependable and Secure Computing (2021).                                  Engineering 01 (2020), 1–1.
[36] Zhen Li, Deqing Zou, Shouhuai Xu, Xinyu Ou, Hai Jin, Sujuan Wang, Zhijun                 [59] Frank Wilcoxon. 1992. Individual comparisons by ranking methods. In Break-
     Deng, and Yuyi Zhong. 2018. VulDeePecker: A Deep Learning-Based System                        throughs in statistics. Springer, 196–202.
     for Vulnerability Detection.. In Network and Distributed Systems Security (NDSS)         [60] Fabian Yamaguchi, Nico Golde, Daniel Arp, and Konrad Rieck. 2014. Modeling and
     Symposium 2018. 1–12.                                                                         discovering vulnerabilities with code property graphs. In 2014 IEEE Symposium
[37] Richard Liaw, Eric Liang, Robert Nishihara, Philipp Moritz, Joseph E Gonzalez,                on Security and Privacy. IEEE, 590–604.
     and Ion Stoica. 2018. Tune: A research platform for distributed model selection          [61] Yaqin Zhou, Shangqing Liu, Jingkai Siow, Xiaoning Du, and Yang Liu. 2019.
     and training. arXiv preprint arXiv:1807.05118 (2018).                                         Devign: Effective vulnerability identification by learning comprehensive program
[38] Guanjun Lin, Wei Xiao, Leo Yu Zhang, Shang Gao, Yonghang Tai, and Jun Zhang.                  semantics via graph neural networks. Advances in Neural Information Processing
     2021. Deep neural-based vulnerability discovery demystified: data, model and                  Systems 32 (2019), 8026–8037.
     performance. Neural Computing and Applications (2021), 1–14.                             [62] Deqing Zou, Yawei Zhu, Shouhuai Xu, Zhen Li, Hai Jin, and Hengkai Ye. 2021.
[39] Bingchang Liu, Liang Shi, Zhuhua Cai, and Min Li. 2012. Software vulnerabil-                  Interpreting deep learning-based vulnerability detector predictions based on
     ity discovery techniques: A survey. In 2012 Fourth International Conference on                heuristic searching. ACM Transactions on Software Engineering and Methodology
                                                                                                   (TOSEM) 30, 2 (2021), 1–31.

## Strona 13

