# ivdetect

Źródło: `ivdetect.pdf`

## Strona 1

Vulnerability Detection with Fine-Grained Interpretations
                                                                      Yi Li                                              Shaohua Wang∗                                   Tien N. Nguyen
                                                  New Jersey Inst. of Technology                                New Jersey Inst. of Technology                     University of Texas at Dallas
                                                        New Jersey, USA                                               New Jersey, USA                                       Texas, USA
                                                         yl622@njit.edu                                              davidsw@njit.edu                              tien.n.nguyen@utdallas.edu

                                         ABSTRACT                                                                                      1    INTRODUCTION
                                         Despite the successes of machine learning (ML) and deep learning                              Software vulnerabilities have caused substantial damage to soci-
                                         (DL) based vulnerability detectors (VD), they are limited to provid-                          ety’s software infrastructures. Automated vulnerability detection
                                         ing only the decision on whether a given code is vulnerable or not,                           (VD) approaches can be broadly classified into two categories: pro-




arXiv:2106.10478v1 [cs.CR] 19 Jun 2021
                                         without details on what part of the code is relevant to the detected                          gram analysis (PA)-based [1, 2, 7–9, 33] and machine learning (ML)-
                                         vulnerability. We present IVDetect, an interpretable vulnerability                            based [23, 28, 30]. The PA-based VD techniques have often focused
                                         detector with the philosophy of using Artificial Intelligence (AI) to                         on solving the specific types of vulnerabilities such as BufferOver-
                                         detect vulnerabilities, while using Intelligence Assistant (IA) via                           flow [3], SQL Injection [6], Cross-site Scripting [5], Authentication
                                         providing VD interpretations in terms of vulnerable statements.                               Bypass [4], etc. In addition to those types, the more general software
                                            For vulnerability detection, we separately consider the vulnera-                           vulnerabilities, e.g., in API usages of libraries/frameworks, have
                                         ble statements and their surrounding contexts via data and control                            manifested in various forms. To detect them, machine learning (ML)
                                         dependencies. This allows our model better discriminate vulnerable                            and deep learning (DL) have been leveraged to implicitly learn the
                                         statements than using the mixture of vulnerable code and con-                                 patterns of vulnerabilities from prior vulnerable code [15, 20, 37].
                                         textual code as in existing approaches. In addition to the coarse-                               Despite several advantages, the ML/DL-based VD approaches are
                                         grained vulnerability detection result, we leverage interpretable AI                          still limited to providing only coarse-grained detection results on
                                         to provide users with fine-grained interpretations that include the                           whether an entire given method is vulnerable or not. In comparison
                                         sub-graph in the Program Dependency Graph (PDG) with the cru-                                 with the PA-based approaches, they fall short in the ability to elab-
                                         cial statements that are relevant to the detected vulnerability. Our                          orate on the fine-grained details of the lines of code with specific
                                         empirical evaluation on vulnerability databases shows that IVDe-                              statements that might be involved in the detected vulnerability.
                                         tect outperforms the existing DL-based approaches by 43%–84%                                  One could use fault localization (FL) techniques [16] to locate the
                                         and 105%–255% in top-10 nDCG and MAP ranking scores. IVDe-                                    vulnerable statements, however they require large, effective test
                                         tect correctly points out the vulnerable statements relevant to                               suites. Due to such feedback at the coarse granularity from the
                                         the vulnerability via its interpretation in 67% of the cases with a                           existing ML/DL-based VD tools, developers would not know where
                                         top-5 ranked list. It improves over baseline interpretation models                            and what to look for and to fix the vulnerability in their code. This
                                         by 12.3%–400% and 9%–400% in accuracy.                                                        hinders them in investigating the potential vulnerabilities.
                                                                                                                                          To raise the level of ML/DL-based VD, we present IVDetect, an
                                         CCS CONCEPTS                                                                                  interpretable VD with the philosophy of using Artificial Intelligence
                                         • Security and privacy → Software security engineering.                                       to detect coarse-grained vulnerability, while leveraging Intelligence
                                                                                                                                       Assistant via interpretable ML to provide fine-grained interpreta-
                                         KEYWORDS                                                                                      tions in term of vulnerable statements relevant to the vulnerability.
                                                                                                                                          For coarse-grained vulnerability detection, our novelty is the
                                         Vulnerability Detection; Deep Learning; Explainable AI; Interpretable
                                                                                                                                       context-aware representation learning of the vulnerable code. During
                                         AI
                                                                                                                                       training, the existing ML/DL-based VD approaches [20, 37] take the
                                         ACM Reference Format:                                                                         entire vulnerable code in a method as the input without distinguish-
                                         Yi Li, Shaohua Wang, and Tien N. Nguyen. 2021. Vulnerability Detection                        ing the vulnerable statements from the surrounding contextual
                                         with Fine-Grained Interpretations. In Proceedings of the 29th ACM Joint Eu-                   code. Such distinction from vulnerable code and the contexts dur-
                                         ropean Software Engineering Conference and Symposium on the Foundations
                                                                                                                                       ing training enable IVDetect to better learn to discriminate the
                                         of Software Engineering (ESEC/FSE ’21), August 23–28, 2021, Athens, Greece.
                                                                                                                                       vulnerable code and benign ones. We represent source code via
                                         ACM, New York, NY, USA, 12 pages. https://doi.org/10.1145/3468264.3468597
                                                                                                                                       program dependence graph (PDG) and we treat the vulnerability
                                         ∗ Corresponding Author                                                                        detection problem as graph-based classification via Graph Con-
                                                                                                                                       volution Network (GCN) [17] with feature-attention (FA), namely
                                         Permission to make digital or hard copies of all or part of this work for personal or         FA-GCN. The vulnerable statements, along with surrounding code,
                                         classroom use is granted without fee provided that copies are not made or distributed
                                         for profit or commercial advantage and that copies bear this notice and the full citation
                                                                                                                                       are encoded during the code representation learning.
                                         on the first page. Copyrights for components of this work owned by others than ACM               For fine-grained interpretation, as the given method is deemed
                                         must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,       as vulnerable by IVDetect, our novelty is to leverage interpretable
                                         to post on servers or to redistribute to lists, requires prior specific permission and/or a
                                         fee. Request permissions from permissions@acm.org.                                            ML [36] to provide the interpretation in term of the vulnerable state-
                                         ESEC/FSE ’21, August 23–28, 2021, Athens, Greece                                              ments as part of the PDG that are involved to the detected vulnerability.
                                         © 2021 Association for Computing Machinery.                                                   The rationale for choosing PDG sub-graph as an interpretation is
                                         ACM ISBN 978-1-4503-8562-6/21/08. . . $15.00
                                         https://doi.org/10.1145/3468264.3468597

## Strona 2

ESEC/FSE ’21, August 23–28, 2021, Athens, Greece                                                                                                  Li, Wang, and Nguyen


that a vulnerability often involves the data and control dependen-
                                                                           1   static long ec_device_ioctl_xcmd(struct cros_ec_dev *ec, void __user *arg)
cies among the statements [26].                                            2   {
                                                                           3       long ret;
    To derive the vulnerable statements as the interpretation, we          4       struct cros_ec_command u_cmd;
                                                                           5       struct cros_ec_command *s_cmd;
leverage the interpretable ML model, GNNExplainer [36], that “ex-          6       if (copy_from_user(&u_cmd, arg, sizeof(u_cmd)))
                                                                           7
plains” on why a model has arrived at its decision. Specifically, after    8
                                                                                       return -EFAULT;
                                                                                   if ((u_cmd.outsize > EC_MAX_MSG_BYTES) || (u_cmd.insize > EC_MAX_MSG_BYTES))
vulnerability detection, to produce interpretation, IVDetect takes         9
                                                                          10
                                                                                       return -EINVAL;
                                                                                   s_cmd = kmalloc(sizeof(*s_cmd) + max(u_cmd.outsize, u_cmd.insize), GFP_KERNEL);
as input the FA-GCN model along with its decision (vulnerable or          11       if (!s_cmd)
                                                                          12           return -ENOMEM;
not), and the input PDG 𝐺 𝑀 of the given method 𝑀. The goal is            13       if (copy_from_user(s_cmd, arg, sizeof(*s_cmd) + u_cmd.outsize)) {
                                                                          14           ret = -EFAULT;
to find the interpretation subgraph, which is defined as a minimal        15           goto exit;
                                                                          16       }
sub-graph G in the PDG of 𝑀 that minimizes the prediction scores          17   + if (u_cmd.outsize != s_cmd->outsize ||
                                                                          18
between using the entire 𝐺 𝑀 and using G. To that end, we leverage        19
                                                                               +
                                                                               +
                                                                                       u_cmd.insize != s_cmd->insize) {
                                                                                       ret = -EINVAL;
GNNExplainer [36] in which the searching for G is formulated as           20
                                                                          21
                                                                               +
                                                                               + }
                                                                                       goto exit;

the learning of the edge-mask set 𝐸𝑀. The idea is that if an edge         22       s_cmd->command += ec->cmd_offset;
                                                                          23       ret = cros_ec_cmd_xfer(ec->ec_dev, s_cmd);
belongs 𝐸𝑀, i.e., if it is removed from 𝐺 𝑀 , and the decision of the     24       /* Only copy data to userland if data was received. */
                                                                          25       if (ret < 0)
model is affected, then the edge is crucial and must be included in the   26           goto exit;
                                                                          27   - if (copy_to_user(arg, s_cmd, sizeof(*s_cmd) + u_cmd.insize))
interpretation for the detection result. Thus, the minimal sub-graph G    28   + if (copy_to_user(arg, s_cmd, sizeof(*s_cmd) + s_cmd->insize))
                                                                          29
in PDG contains the nodes and edges, i.e., the crucial statements and     30   exit:
                                                                                       ret = -EFAULT;

program dependencies, that are most decisive/relevant to the detected     31       kfree(s_cmd);
                                                                          32       return ret;
vulnerability when the decision is vulnerable.                            33   }

    Using our results, a practitioner would 1) examine the ranked
list of potentially vulnerable methods, and 2) use the interpretation            Figure 1: CVE-2016-6156 Vulnerability in Linux 4.6
to further investigate what statements in the code that caused the
model to predict that vulnerability.
    We conducted several experiments to evaluate IVDetect in both              “At line 6 and line 13, the driver fetches user space data by pointer
vulnerability detection at the method level and interpretation in          arg via copy_from_user(). The first fetched value (stored in u_cmd) (line
term of vulnerable statements. We use 3 large C/C++ vulnerability          6) is used to get the in_size and out_size elements and allocation a
datasets: Fan [13], Reveal [11] and FFMPeg+Qemu [37]. For the              buffer (s_cmd) at line 10 so as to copy the whole message to driver
method-level VD, our results show that IVDetect outperforms the            later at line 13, which means the copy size of the whole message
existing ML/DL-based approaches [11, 19, 20, 27, 37] by 43%–84%            (s_cmd) is based on the old value (u_cmd.outsize) from the first fetch.
and 105%–255% at the top 10 list for two ranking scores nDCG and           Besides, the whole message copied at the second fetch also contains
MAP, respectively. For the statement-level interpretation, IVDe-           the elements of in_size and out_size, which are the new values. The
tect correctly points out the vulnerable statements relevant to            new values from the second fetch might be changed by another user
the vulnerability in 67% of the cases with a top-5 ranked list. It         thread under race condition, which will result in a double-fetch bug
improves over the baseline ATT [36] and GRAD [36] interpretation           when the inconsistent values are used.”
models by 12.3%–400% and 9%–400% in accuracy, respectively.                   Thus, to fix this bug, a developer added the code at lines 17–21
    The contributions of this paper include:                               to make sure that u_cmd.outsize and u_cmd.insize have not changed
A. Interpretable VD with Fine-grained Interpretations                      due to race condition between the two fetching calls. Moreover,
    a. Vulnerability Detection with Fine-grained Interpreta-               memory access might be also beyond the array boundary, causing
tions: IVDetect is the first approach to leverage interpretable            a buffer overflow within the method call cros_ec_cmd_xfer(...), when
ML to enhance VD with fine-grained details on PDG sub-graphs,              the command is transferred to the ChromeOS device at line 23.
statements, and dependencies relevant to the detected vulnerability.          Another issue is at line 27 with copy_to_user. The method call
    b. Context-aware Representation Learning of vulnerable                 cros_ec_cmd _xfer(...) can set s_cmd->insize to a lower value. Thus, the
code: The novelty of our representation learning of vulnerable code        new smaller value must be used to avoid copying too much data to
is our consideration of the contextual code surrounding the vulnerable     the user: u_cmd.insize at line 27 is changed into s_cmd->insize.
statements and fixes to better train the VD model.                            This vulnerable code could potentially cause the damages such as
B. Empirical Evaluation. Our results show IVDetect’s high ac-              denial of service, buffer overflow, program crash, etc. Deep learning
curacy in both detection and interpretation (See data/results at [10]).    (DL) advances enable several approaches [20, 37] to implicitly learn
                                                                           from the history the patterns of vulnerable code, and to detect more
                                                                           general vulnerabilities. However, they are still limited in comparison
2 MOTIVATION                                                               with program analysis-based approaches in the ability to provide
                                                                           any detail on the fine-grained level of the vulnerable statements, and
2.1 Motivating Example                                                     on why the model has decided on the vulnerability. For example,
Figure 1 shows the method ec_device_ioctl_xcmd in Linux 4.6, which         the PA-based approaches, e.g., a race detection technique could
constructs the I/O control command for the CromeOS devices. This           potentially detect the involvement of the two fetching statements
is listed as a vulnerable code within Common Vulnerabilities and           at line 6 and line 13. The method in Figure 1 might be deemed
Exposures (CVE-2016-6156) in the National Vulnerability Database.          as vulnerable by a DL-based model. But without any fine-grained
    The commit log of the corresponding fix stated that                    details, a developer would not know where and what to investigate

## Strona 3

Vulnerability Detection with Fine-Grained Interpretations                                            ESEC/FSE ’21, August 23–28, 2021, Athens, Greece


                                                                         2.2    Key Ideas and Architecture Overview
                                                                         IVDetect has two main modules (Figure 3): graph-based vulnera-
                                                                         bility detection model, and graph-based interpretation model. The
                                                                         input is the source code of all methods in a project. The output is
                                                                         the ranked list of methods with the detection result/score and the
                                                                         interpretation (PDG sub-graph). Let us explain our key ideas.

                                                                         2.2.1 Graph-based Vulnerability Detection Model (Section 3).
                                                                         As seen in Section 2.1, a vulnerability is usually exhibited as multiple
                                                                         statements are exploited, thus, it is natural to capture the vulnerable
                                                                         code as a sub-graph in the PDG with the data and control flows. To
                                                                         do so, we model the vulnerability detection via the Graph Convo-
                                                                         lutional Network (GCN) [17] as follows. The PDG of a method 𝑀
                                                                         is represented as a graph 𝐺 𝑁 = (𝑉 , 𝐸) in which 𝑉 is a set of nodes
                                                                         representing the statements, and 𝐸 is a set of edges representing
                                                                         the data/control dependencies. A feature description 𝑥𝑉 is for every
                                                                         node 𝑣, which represents a property of a node, e.g., variable name,
                                                                         etc. Features are summarized in a 𝑁 × 𝐷 feature matrix 𝑋𝑀 (𝑁 :
                                                                         number of nodes and 𝐷 is the number of input features). Let 𝑓 be
        Figure 2: Interpretation Sub-Graph for Figure 1                  a label function on the statements and methods 𝑓 : 𝑉 → {1, ..., 𝐶}
                                                                         that maps a node in 𝑉 and an entire method to one of the 𝐶 classes.
                                                                         In IVDetect, 𝐶=2 for vulnerable (V) and non-vulnerable (N V).
                                                                             For training on (non-)vulnerable code in the training set, GCN
                                                                         performs similar operations as CNN where it learns the features
                                                                         with a small filter/window sliding over PDG sub-structure. Differing
                                                                         from image data with CNN, the neighbors of a node in GCN are un-
                  Figure 3: Overview of IVDetect                         ordered and variable in size. To predict if a method 𝑀 is vulnerable,
                                                                         its PDG 𝐺 𝑀 with the associated feature set 𝑋𝑀 = {𝑥 𝑗 |𝑣 𝑗 ∈ 𝐺 𝑀 } are
                                                                         built. GCN learns a conditional distribution 𝑃 (𝑌 |𝐺 𝑀 , 𝑋𝑀 ), where
                                                                         𝑌 is a random variable representing the labels {1, ..., 𝐶}. That distri-
next. This would make the output of a DL model less constructive         bution indicates the probability of the graph 𝐺 𝑀 belonging to each
in VD. Moreover, a fault localization technique [16], which locates      of the classes {1, ..., 𝐶}, i.e., 𝑀 is vulnerable or not (Section 3).
buggy statements, would need a large, effective test suite.
   Regarding detection, the existing DL-based approaches [20, 37]        2.2.2 Distinction between Vulnerable Statements and Sur-
do not fully exploit all the available information on the vulnera-       rounding Contexts. During training, for each vulnerable state-
ble code during training. For example, during training, we know          ment 𝑠 in a method in the training dataset, we distinguish 𝑠 and the
that lines 23 and 27 are vulnerable/buggy, and other relevant state-     surrounding contextual statements for 𝑠. A context consists of the
ments via data/control dependencies provide contextual information       statements with data and/or control dependencies with 𝑠. This is
for the vulnerable ones. However, the existing approaches [20, 37]       expected to help our model recognize better the vulnerable code
do not consider the vulnerable statements and do not use the con-        appearing in specific surrounding contexts, and have better discrim-
textual code to help a model discriminate the vulnerable and non-        inating the vulnerable code from the benign one. For example, the
vulnerable ones. The entire method would be fed to a DL model.           existing approaches feed the entire PDG of the method in Figure 2
                                                                         into a model. IVDetect distinguishes and learns the vector repre-
IVDetect Approach. We introduce IVDetect, an DL-based, in-
                                                                         sentation for the vulnerable statement at line 27 while considering
terpretable vulnerability detection approach that goes beyond the
                                                                         as contexts the statements with data/control dependencies with
decision of vulnerability by providing the fine-grained interpreta-
                                                                         line 27: the data-dependency context (lines 31, 22, 13, 10, and 6),
tion in term of the vulnerable statements. Specifically, as the method
                                                                         and the control-dependency context (lines 29, 25, 23, and 13).
is deemed as vulnerable by IVDetect, it will provide a list of impor-
tant statements as part of the program dependence graph (PDG) that       2.2.3 Graph-based Interpretation Model for Vulnerability
are relevant to the detected vulnerability. For example, it provides     Detection (Section 4). After prediction, IVDetect performs fine-
the partial sub-graph of the PDG including the statements at the         grained interpretation. It uses both the PDG 𝐺 𝑀 of the method
lines 13–15, 22–23, and 25–27 in Figure 2 for the vulnerable code at     𝑀 and the GCN model as the input to obtain the interpretation.
line 23 and line 27. We use the PDG sub-graph including important        To that end, we leverage the interpretable ML technique GNNEx-
statements for fine-grained VD since they will give a developer the      plainer [36]. Its goal is to take the GCN and a specific input graph
hints on the program dependencies relevant to the vulnerability          𝐺 𝑀 , and produce the crucial sub-graph structures and features in 𝐺 𝑀
for further investigation. Moreover, if our model determines the         that affect the decision of the model. GNNExplainer’s idea is that if
code as non-vulnerable, it can also produce the key sub-graph of         removing or altering a node/feature does affect the prediction outcome,
the PDG with key statements that are deemed to be safe.                  the node/feature is considered as essential and thus must be included

### Obrazy na stronie

- `image` obiekt 0: ![image strona 3 obiekt 0](pdfimages/ivdetect/ivdetect-000.png)
- `smask` obiekt 1: ![smask strona 3 obiekt 1](pdfimages/ivdetect/ivdetect-001.png)
- `image` obiekt 2: ![image strona 3 obiekt 2](pdfimages/ivdetect/ivdetect-002.png)
- `smask` obiekt 3: ![smask strona 3 obiekt 3](pdfimages/ivdetect/ivdetect-003.png)

## Strona 4

ESEC/FSE ’21, August 23–28, 2021, Athens, Greece                                                                                     Li, Wang, and Nguyen


in the crucial set (let us call it the interpretation set). GNNExplainer   to skip the zeros at the end of the sequence of sub-tokens. Those
searches for a sub-graph G𝑀 in 𝐺 𝑀 that minimizes the difference in        zeros will not be included in the training.
the prediction scores between using the whole graph 𝐺 𝑀 and using          5. Attention-based Bidirectional GRU. After having all vectors
the minimal graph G𝑀 (Section 4). Because without that subgraph            for the features 𝐹 1 , 𝐹 2 , ..., we use a bi-directional GRU and an atten-
G𝑀 in the input PDG 𝐺 𝑀 , GCN model would not decide 𝐺 𝑀 as                tion layer to learn the weight vector 𝑊𝑖 for each feature 𝐹𝑖 , based on
vulnerable, G𝑀 is considered as crucial PDG sub-graph consisting           the hidden states from that model. Then, we compute the weighted
of crucial statements and data/control dependencies relevant to            vector for each feature by multiplying the original vector for the
the detected vulnerability (if the outcome is V). If the outcome is        feature by the weight: 𝐹𝑖′ = 𝑊𝑖 .𝐹𝑖 .
non-vulnerability, G𝑀 can be considered as the safe statements in             Finally, we need to consider the impacts from the dependent state-
PDG for the model to decide the input method 𝑀 as benign code.             ments to the current statement in the PDG. The rationale is that those
                                                                           neighboring statements in the PDG must have the influence on the
                                                                           current statement if one of them is vulnerable. For example, the
3  GRAPH-BASED VULNERABILITY                                               neighboring statements for 𝑆 27 in the PDG include the statements
   DETECTION MODEL                                                         at lines 6, 22, 25, and 29. Thus, we combine and summarize them
3.1 Representation Learning                                                into the final feature vector 𝐹𝑆27 for the statement 𝑆 27 as follows:
Let us present how we build the vector representations for code                                         ∑︁
features. For a statement, we extract the following types of features:                         𝐹𝑆27 =        𝑊𝑖 𝐶𝑜𝑛𝑐𝑎𝑡 (ℎ(𝐹𝑖′, 𝑗))                    (1)
1. Sequence of Sub-tokens of a Statement. At the lexical level,                                         𝑖
we capture the content of a statement in term of the sequence
of sub-tokens. We choose the sub-token granularity because the             𝑊𝑖 is the trainable weight for combination; 𝐶𝑜𝑛𝑐𝑎𝑡 is the concate-
sub-tokens are more likely to be repeated than the entire lexical          nate layer to link all values into one vector; ℎ is the hidden layer to
tokens in source code [31]. We tokenize each statement and keep            summarize vector into a value; 𝑖 = S6, S22, S25, S27, S29; 𝑗 is feature
only the variables, method and class names. The names are broken           index. 𝐹 27 is used in the next step with GCN model for detection.
into sub-tokens using CamelCase or Hungarian convention. We
remove the sub-tokens with one character to avoid the influence            3.2    Vulnerability Detection with FA-GCN
of noises. For example, in Figure 4, the tokens of 𝑆 27 are collected
                                                                           Figure 5 presents how we use Feature-Attention GCN model (FA-
and broken down into the sequence: copy, to, user, arg, etc. Then,
                                                                           GCN) [29] for detection. The rationale is that FA-GCN can deal well
we use GloVe [25], to build the vectors for tokens, together with
                                                                           with the graphs with sparse features (not all the statements share
Gate Recurrent Unit (GRU) [12] to build the feature vector for the
                                                                           the same properties), and potentially noisy features in a PDG. First,
sequence of sub-tokens for 𝑆 27 . GloVe is known to capture well
                                                                           we parse the method 𝑀 into PDG. Similar to CNN using the filter
semantic similarity among tokens. GRU is chosen to summarize
                                                                           on an image, FA-GCN performs sliding a small window along all
the sequence of vectors into one feature vector for the next step.
                                                                           the nodes (statements) of the PDG. For example, in Figure 5, the
2. Code Structure of a Statement. We capture code structure via            window marked with A for the node 𝑆27 consists of itself and
the AST sub-tree. In Figure 4, the AST sub-tree for 𝑆 27 is extracted
                                                                           the neighboring statements/nodes 𝑆6, 𝑆22, 𝑆25, and 𝑆29. Another
and fed to Tree-LSTM [32] to capture the structure into a vector 𝐹 2 .
                                                                           window (marked with B ) is for the node 𝑆23, including itself and
3. Variables and Types. For each node (i.e., a statement), we col-         the neighboring nodes: 𝑆22 and 𝑆25. For each window, FA-GCN
lect the names of the variables and their static types at their lo-        generates the feature representation matrix for the statement at the
cations, break them into the sub-tokens. For example, we collect           center. For example, for the window centered at 𝑆27, it generates the
the variable s_cmd and its static type cross_ec_command. We use the        feature vector 𝐹𝑆27 for 𝑆27, using the process explained in Figure 4.
same vector building techniques as for the sub-token sequences as          From the representation vectors for all statements, FA-GCN uses a
in feature 1, including GloVe and GRU, to apply on the sequences of        join layer to link all these vectors into the Feature Matrix F𝑚 for
sub-tokens built from the variables’ names (e.g., s_cmd) and those         method 𝑀. A row in F𝑚 corresponds to a window in PDG.
from the variables’ types (e.g, cross_ec_command).                             Next, FA-GCN performs the convolution operation by first calcu-
4. Surrounding Contexts. During training, for a statement 𝑠, we            lating the symmetric normalized Laplacian matrix 𝐴˜ [17], and then
also encode the statements surrounding 𝑠, which we refer to as             calculating the convolution to generate the representation matrix
context. Data- and Control-dependency contexts contain the state-          𝑀𝑚 for the method 𝑚. After that, we use the traditional steps as in
ments having such dependencies with the current statement. For             a CNN model: using a spatial pyramid pooling layer (to normalize
example, the data-dependency context for 𝑆 27 includes the state-          the method representation matrix into a uniform size, and reduce
ments at the lines 31, 22, 13, 10, and 6. If the control dependencies      its total size), and connecting its output to a fully connected layer
are considered, the statements with control dependencies with 𝑆 27         to transform the matrix into a vector 𝑉𝑚 to represent 𝑚. With 𝑉𝑚 ,
at the lines 29, 25, 23, and 13 are included. The vectors for the state-   we perform classification by using two hidden layers (controlling
ments in the context are calculated via GloVe and GRU as described         the length of vectors and output) and a softmax function to produce
earlier. The number of dependencies could be different, then the           a prediction score for 𝑚. We use those scores as vulnerability scores
lengths of the GRU model inputs could be different. Therefore, we          to rank the methods in a project. The decision for 𝑚 as V or N V is
apply zero padding with a masking layer, which allows the model            done via a trainable threshold on the prediction score [18, 20].

## Strona 5

Vulnerability Detection with Fine-Grained Interpretations                                                ESEC/FSE ’21, August 23–28, 2021, Athens, Greece




                Figure 4: Code Representation Learning for Statement S27 in Graph-based Vulnerable Code Detection




                                                      Figure 5: Vulnerability Detection with FA-GCN


4    GRAPH-BASED INTERPRETATION MODEL
Let us explain how we use GNNExplainer [36] to build our graph-
based interpretation. The input includes the trained FA-GCN model,
the PDG (𝐺 𝑀 ) of the method 𝑀, and the detection result V or N V,
and prediction score. Figure 6 illustrates our process for the case of
V (Vulnerable) (the case of N V is done similarly).                              Figure 6: Masking to Derive Interpretation Sub-Graphs
   To derive the interpretations, the key goal is to find a sub-graph
G𝑀 in the PDG 𝐺 𝑀 of the method 𝑀 that minimizes the difference
in the prediction scores between using the entire graph 𝐺 𝑀 and                of possible sub-graphs and the edge-mask sets are untractable,
using the minimal graph G𝑀 . To do so, we use GNNExplainer                     GNNExplainer uses a learning approach for the edge-mask 𝐸𝑀.
with the masking technique [36], which treats the searching for the               Let us formally explain how GNNEXplainer [36] works. It for-
minimal graph G𝑀 as a learning problem of the edge-mask set 𝐸𝑀                 mulates the problem by maximizing the mutual information (MI)
of the edges. The idea is that learning 𝐸𝑀 helps IVDetect derive               between the minimal graph G𝑀 and the input 𝐺 𝑀 :
the interpretation sub-graph G𝑀 by masking-out
                                         Ç           the edges in 𝐸𝑀
from 𝐺 𝑀 (“masked-out” is denoted by        ):                                             max 𝑀𝐼 (𝑌, G𝑀 ) = 𝐻 (𝑌 ) − 𝐻 (𝑌 |𝐺 = G𝑀 )                 (3)
                                                                                            G𝑀
                                          È
                             G𝑀 = 𝐺 𝑀           𝐸𝑀                     (2)     𝑌 is the outcome decision by the FA-GCN model. Thus, the entropy
                                                                               term 𝐻 (𝑌 ) is constant for the trained FA-GCN model. Maximizing
Figure 6 illustrates GNNExplainer’s principle. As an edge-mask set             the 𝑀𝐼 value for all G𝑀 is equivalent to minimizing conditional
is applied, GNNEXplainer checks if the FA-GCN model produces                   entropy 𝐻 (𝑌 |𝐺 = G𝑀 ), which by definition of conditional entropy
the same result (in this case the result is V). If yes, the edge in the        can be expressed as
edge-mask is not important and is not included in G𝑀 . Otherwise,
the edge is important and included in G𝑀 . Because the numbers                                − E𝑌 | G𝑀 [𝑙𝑜𝑔𝑃 𝐹𝐴−𝐺𝐶𝑁 (𝑌 |𝐺 = G𝑀 ]                    (4)

### Obrazy na stronie

- `image` obiekt 4: ![image strona 5 obiekt 4](pdfimages/ivdetect/ivdetect-004.png)
- `smask` obiekt 5: ![smask strona 5 obiekt 5](pdfimages/ivdetect/ivdetect-005.png)
- `image` obiekt 6: ![image strona 5 obiekt 6](pdfimages/ivdetect/ivdetect-006.png)
- `image` obiekt 7: ![image strona 5 obiekt 7](pdfimages/ivdetect/ivdetect-007.png)

## Strona 6

ESEC/FSE ’21, August 23–28, 2021, Athens, Greece                                                                                Li, Wang, and Nguyen


                        Table 1: Three Datasets                                 Baselines. We compare IVDetect with the state-of-the-art DL-
                                                                             based vulnerability detection approaches: 1) VulDeePecker [20]: a
                        Dataset          Fan       Reveal    Devign
                 Vulnerabilities      10,547         1,664    10,067
                                                                             DL-based approach using Bidirectional LSTM on the statements and
            Non-vulnerabilities      168752         16505     12,294         their data/control dependencies. 2) Devign [37]: an DL-based ap-
            Ratio (Vul:Non-vul)         1:16         1:9.9     1:1.2         proach that uses GGCN model with Gated Graph Recurrent Layers
                                                                             on the AST, CFG, DFG, and code sequences for graph classification.
                                                                             3) SySeVR [19]: in addition to statements and program dependen-
The meaning of this conditional entropy formula is a measure of              cies, this approach also uses program slicing and leverages several
how much uncertainty remains about the outcome 𝑌 when we                     DL models (LR, MLP, DBN, CNN, LSTM, etc.). 4) Russell et al. [27]:
know 𝐺 = G𝑀 . GNNEXplainer also limits the size of G𝑀 by 𝐾𝑀 ,                This DL approach encodes source code as matrices of code tokens
i.e., taking 𝐾𝑀 edges that give the highest mutual information with          and leverages convolution model with random forest (RF) via en-
the prediction outcome 𝑌 . Direct optimization of the formula 4 is           semble classifier. 5) Reveal [11]: This approach uses GGNN, MLP,
not tractable, thus, GNNExplainer treats G𝑀 as a random graph                and with Triplet Loss on graph representations of source code.
variable G. The objective in Equation 4 becomes:                                Procedure. A dataset contains a number of vulnerable and non-
                       min E G𝑀 ∼G 𝐻 (𝑌 |𝐺 = G𝑀 )                      (5)   vulnerable methods. We first randomly split all of its vulnerable
                         G                                                   methods into 80%, 10%, and 10% to be used for training, tuning,
                         min 𝐻 (𝑌 |𝐺 = E G [G𝑀 ])                      (6)   and testing, respectively. For training, we add to that 80% part the
                             G                                               same number of non-vulnerable methods as the vulnerable ones to
From Equation 5, we obtain Equation 6 with Jensen’s inequality. The          obtain the balanced training data. For tuning and testing, we also
conditional entropy in Equation 6 can be optimized by replacing              add the non-vulnerable methods but we use the real ratio between
E G [G𝑀 ] to be optimized by masking with 𝐸𝑀 on the input graph              vulnerable and non-vulnerable methods in the original dataset to
𝐺 𝑀 . Now, we can reduce the problem to learning the mask 𝐸𝑀.                build tuning/testing data. We use AutoML [21] on all models to
Details on training can be found in [36]. The resulting sub-graph            automatically tune hyper-parameters on the tuning dataset.
G𝑀 is directly used as an interpretation. We can similarly produce              We also performed the evaluation across the datasets. We first
the interpretations for the cases of non-vulnerability result.               trained our model on the combination of two datasets Reveal and
                                                                             FFMPeg+Qemu, which has a balanced number of vulnerable methods
5 EMPIRICAL EVALUATION                                                       and non-vulnerable ones. We then tested the model on Fan dataset,
5.1 Research Questions                                                       which has a more realistic ratio of vulnerable and non-vulnerable
                                                                             methods. To ensure the model suitable for cross-data evaluation,
To evaluate IVDetect, we seek to answer the following questions:
                                                                             we also used 20% of Fan dataset for tuning the parameters and
RQ1. Comparison on the Method-Level Vulnerability Detec-
                                                                             performed prediction on the remaining 80%.
tion (VD). How well does IVDetect perform in comparison with
                                                                                Evaluation Metrics: We use the following evaluation metrics.
the state-of-the-art method-level Deep Learning VD approaches?                                                        Í𝑄
                                                                                                                           𝐴𝑣𝑔𝑃 (𝑞)
RQ2. Comparison with other Interpretation Models for Fine-                       Mean Average Precision 𝑀𝐴𝑃 = 𝑞=1 𝑄                  , with Average
grained VD Interpretation. How well does IVDetect perform                                         Í
                                                                             Precision 𝐴𝑣𝑔𝑃 = 𝑛𝑘=1 𝑃 (𝑘)𝑟𝑒𝑙 (𝑘), where 𝑛 is the total number
in comparison with the state-of-the-art interpretation models for            of results 𝑘 is the current rank in the list, 𝑟𝑒𝑙 (𝑘) is an indicator
fine-grained VD interpretation to point out vulnerable statements?           function equaling to 1 if the item at rank 𝑘 is actually vulnerable,
RQ3. Vulnerable Code Patterns and Fixing Patterns. Is IVDe-                  and to zero otherwise. 𝑄 is the total number of classification types.
tect useful in detecting vulnerable code patterns and fixes?                 It is 1 because we only have two types including vulnerable and
RQ4. Sensitivity Analysis for Internal Features. How do inter-               non-vulnerable classes, however, we rank all the methods based on
nal features affect the overall performance of IVDetect?                     their scores (1 indicates vulnerable, and 0 otherwise).
RQ5. Sensitivity Analysis on Training Data. How do different                     Normalized DCG at 𝑘: 𝑛𝐷𝐶𝐺𝑘 = 𝐼𝐷𝐶𝐺      𝐷𝐶𝐺𝑘 , with Discounted Cu-
                                                                                                                             𝑘

data splitting schemes affect IVDetect’s performance?
                                                                             mulative Gain at rank 𝑘, 𝐷𝐶𝐺𝑘 = 𝑖=1 𝑙𝑜𝑔 𝑟(𝑖+1)
                                                                                                                    Í𝑘           𝑖
                                                                                                                                   ; and Ideal DCG
RQ6. Time Complexity. What is time complexity of IVDetect?                                                                     2
                                                                                              Í |𝑅𝑘 | 2𝑟𝑖 −1
                                                                             at 𝑘 𝐼𝐷𝐶𝐺𝑘 = 𝑖=1 𝑙𝑜𝑔 (𝑖+1) ; where 𝑟𝑖 is the score of the result
                                                                                                        2
5.2     Datasets                                                             at position 𝑖, and 𝑅𝑘 the rank of the actual vulnerable methods
We have conducted our study on three vulnerability datasets in-              (ordered by their scores) in the resulting list up to the position 𝑘.
cluding Fan et al.’s [13], Reveal [11] and FFMPeg+Qemu [37] (Ta-                 First Ranking (𝐹𝑅) is the rank of the first correctly predicted
ble 1). Fan et al. [13] dataset covers the CWEs from 2002 to 2019            vulnerable method. Average ranking (𝐴𝑅) is the average rank of
with 21 features for each vulnerability. At the method level, the            the correctly predicted vulnerable methods in the top-ranked list.
dataset contains +10K vulnerable methods and fixed code. The                     Accuracy under curve (AUC) is defined as 𝐴𝑈𝐶 = 𝑃 (𝑑 (𝑚 1 ) >
Reveal dataset [11] contains +18K methods with 9.16% of the vul-             𝑑 (𝑚 2 )) in which 𝑃 is the probability, 𝑑 is the detection model (can
nerable ones. The FFMPeg+Qemu dataset has been used in Devign                be regarded as a binary classifier), 𝑚 1 is a randomly chosen positive
study [37] with +22K data, and 45.0% of the entries are vulnerable.          instance, and 𝑚 2 is a randomly chosen negative instance.
                                                                                 Precision (P) is the fraction of relevant instances among the
5.3     Experimental Methodology                                             retrieved ones. It is calculated as 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 = 𝑇 𝑃𝑇+𝐹 𝑃
                                                                                                                                      𝑃 while 𝑇 𝑃 is
RQ1. Comparison on Method-Level DL-based VD Approaches.

## Strona 7

Vulnerability Detection with Fine-Grained Interpretations                                                   ESEC/FSE ’21, August 23–28, 2021, Athens, Greece


the number of true positives and the 𝐹 𝑃 is the number of false             Table 2: RQ1. Top-10 Vulnerability Detection Ranked Re-
positives.                                                                  sults on FFMPeg+Qemu Dataset. 0: incorrect, 1: correct
    Recall (R) is the fraction of relevant instances that were retrieved.    Top-10 result     1   2    3      4     5     6    7     8     9    10   Total
It is calculated as 𝑅𝑒𝑐𝑎𝑙𝑙 = 𝑇 𝑃𝑇+𝐹𝑃
                                     𝑁 while 𝑇 𝑃 is the number of true       VulDeePecker      0   0    0      0     0     0    1     0     1     1     3
positives and the 𝐹 𝑁 is the number of false negatives.                         SySeVR         0   0    0      0     0     1    1     1     0     1     4
                                                                              Russell et al.   0   0    0      0     1     0    1     0     1     1     4
    F score (F) is the harmonic mean of precision and recall. It is             Devign         0   0    0      0     1     0    1     1     1     0     4
                            𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑅𝑒𝑐𝑎𝑙𝑙 .
calculated as 𝐹𝑠𝑐𝑜𝑟𝑒 = 2 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙                                        Reveal        0   0    0      1     0     1    0     1     1     1     5
                                                                               IVDetect        1   0    1      1     1     0    1     1     0     0     6
RQ2. Comparison with other Interpretation Models for Fine-
grained Interpretation.
                                                                            added lines from 17–21. Thus, G𝑀 is correct. The rationale is that if
    Baselines. We compare IVDetect with the following interpre-
                                                                            the interpretation sub-graph G𝑀 contains some statement relevant
tation models. 1) ATT [36]: This approach is a graph attention
                                                                            to the added statement to fix the vulnerability, that interpretation
network that uses the attention mechanism to evaluate the weights
                                                                            is useful in pointing out the code relevant to the vulnerability.
(importance levels) of the edges in the input graph. 2) GRAD [36]:
                                                                               We also use Mean First Ranking (MFR), i.e., the mean of the
This approach is a gradient-based method that computes the gradi-
                                                                            rankings for the first statement that needs to be fixed in the inter-
ent of the GNN’s loss function w.r.t. the adjacency matrix.
                                                                            pretation statements, and Mean Average Ranking (MAR), i.e., the
     Procedure. Our goal here is to evaluate how well IVDetect
                                                                            mean of the rankings for all statements to be fixed in the interpreta-
produces the fine-grained interpretations pointing to vulnerable
                                                                            tion statements. If a statement to be fixed has not been selected as
statements. Thus, to train/test the interpretation model, we need to
                                                                            interpretation, we do not consider it when calculating MFR/MAR.
use the Fan dataset because it contains the vulnerable statements
and respective fixes. The other two datasets contain only the vul-          RQ3. Vulnerable Code Patterns and Fixing Patterns.
nerabilities at the method level and no fixes. Therefore, in this RQ2,          Procedure. We use a mining algorithm on the set of interpretation
for the vulnerability prediction part, we used the GCN-FA model             sub-graphs to mine patterns of vulnerable code. We also mine fixing
that was trained on Reveal and FFMPeg+Qemu and predicted on the             patterns for those vulnerabilities. See details in Section 6.3.
Fan dataset. For the methods that are vulnerable, but predicted as             Evaluation Metrics. We counted the identified patterns.
non-vulnerable, we considered those cases as incorrect because the          RQ4. Sensitivity Analysis for Features.
resulting interpretations do not make sense for incorrect detection.            Procedure. We first built a base model with only the feature
For the methods that are actually non-vulnerable (regardless of the         that represents the code as the sequence of tokens. We then built
predictions), we could not use them because the non-vulnerable              other variants of our model by gradually adding one more feature
methods do not have the fixed statements as the ground truth for            in Section 3.1 to the base model including the sequence of sub-
interpretations. Thus, we use the set of methods that are vulnera-          tokens, AST subtree, variable names, data dependencies, and control
ble and correctly detected as vulnerable for the evaluation of the          dependencies. We measured accuracy for each variant. We used the
interpretation model. Let us use 𝐷 to denote this set.                      Fan dataset and the same experiment setting as in RQ1.
    For the interpretation, we randomly split 𝐷 into 80%, 10%, and             Evaluation Metrics. We use the same metrics as in RQ1.
10% for training, tuning, and testing. For training, we used the fixed      RQ5. Sensitivity Analysis for Training Data. We used different
statements as the labels for interpretation because those fixed ones        ratios in data splitting for training, tuning, and testing: (80%, 10%,
were the vulnerable ones. For testing, we compared the relevant             10%), (70%, 15%, 15%), (60%, 20%, 20%), and (50%, 25%, 25%). We used
statements from the interpretation model against the actual fixed           the same Fan dataset and setting as in RQ1.
statements. Each method in the testing set and the trained GCN-FA              Evaluation Metrics. We use the same metrics as in RQ1.
model are the input of the interpretation model in this RQ2.                RQ6. Time Complexity Analysis. We measure the actual train-
    Evaluation Metrics. Given an interpretation sub-graph G𝑀 gen-           ing and predicting time.
erated from the graph-based interpretation model, we evaluate the
accuracy of the interpretation for a model as follows. For a method,        6 EXPERIMENTAL RESULTS
if G𝑀 has an overlap with any statement in the code changes that fix
                                                                            6.1 RQ1. Comparison on Method-Level VD
the vulnerability, G𝑀 is considered as a correct interpretation, i.e.,
relevant to the VD. We then calculate Accuracy as the ratio between         In Table 2, among the top 10 prediction results, IVDetect has the
the number of correct interpretations over the total number of inter-       most correct predictions (6 vulnerable methods). The vulnerable
pretations. Because code changes could include addition, deletion,          methods correctly detected by IVDetect are also pushed higher
and modification, we further define such overlap as follows.                in the top-10 ranked list with 4 correct results out of 5 top results.
    If one of the statements 𝑆 in the vulnerable version was deleted        All other baselines have only 0–1 correct detection in the top-5 list.
or modified for fixing, and if G𝑀 ∋ 𝑆, then we consider the inter-          Importantly, the first rank for IVDetect (i.e., the rank of the first
pretation sub-graph G𝑀 is correct, otherwise incorrect. If one of           correctly detected vulnerable methods) is 1st, while those of the
the statements 𝑆 ′ was added to the vulnerable version for fixing,          baselines are 4𝑡ℎ , 5𝑡ℎ , 5𝑡ℎ , 6𝑡ℎ , and 7𝑡ℎ (the bold values in Table 2).
we check on the fixed version whether G𝑀 contains any statement             Moreover, IVDetect can detect 14, 35, and 64 vulnerabilities among
with data or control dependencies with 𝑆 ′ , we consider it as cor-         top-20, top-50, and top-100 prediction results.
rect, otherwise, incorrect. For example, in Fig. 2, G𝑀 contains the            Tables 3, 4, and 5 show the comparison among the approaches
statement S23 with data and control dependencies with one of the            on three datasets. IVDetect consistently performs better in all
                                                                            the metrics (Table 3). For nDCG@{1,3}, all the baselines get zeros

## Strona 8

ESEC/FSE ’21, August 23–28, 2021, Athens, Greece                                                                                               Li, Wang, and Nguyen


Table 3: RQ1. Method-Level VD on FFMPeg+Qemu Dataset                                    Table 4: RQ1. Method-Level VD on Fan Dataset
                VulDee-     SySeVR    Russell      Devign   Reveal   IVDetect                       VulDee-   SySeVR   Russell     Devign      Reveal      IVDetect
                -Pecker                et al.                                                       -Pecker             et al.
 nDCG@1             0           0        0            0        0         1       nDCG@1                 0        0        0           0           0                0
 nDCG@3             0           0        0            0        0       0.63      nDCG@5                 0        0        0           0           0               0.5
 nDCG@5             0           0      0.43         0.45     0.5       0.65      nDCG@10                0        0      0.30        0.33        0.34             0.43
 nDCG@10          0.37        0.44     0.45         0.46     0.5       0.68      nDCG@15                0        0      0.28        0.30        0.37             0.45
 nDCG@15          0.45        0.48     0.49         0.52     0.55      0.75      nDCG@20              0.08     0.23     0.31        0.32        0.38             0.46
 nDCG@20          0.48        0.51     0.54         0.56     0.6       0.82       MAP@1                 0        0        0           0           0                0
  MAP@1             0           0        0            0        0         1        MAP@5                 0        0        0           0           0              0.25
  MAP@3             0           0        0            0        0       0.83      MAP@10                 0        0       0.1        0.13        0.18             0.27
  MAP@5             0           0      0.20         0.20     0.25      0.80      MAP@15                 0        0      0.12        0.14        0.21             0.28
 MAP@10           0.22        0.31     0.30         0.32     0.38      0.78      MAP@20               0.08     0.24     0.14        0.15        0.20             0.28
 MAP@15           0.29        0.33     0.34         0.37     0.41      0.72        FR@1               n/a      n/a       n/a        n/a         n/a              n/a
 MAP@20           0.32        0.35     0.37         0.42     0.45      0.69        FR@5               n/a      n/a       n/a        n/a         n/a                4
   FR@1           n/a         n/a       n/a         n/a      n/a         1        FR@10               n/a      n/a       10           8           6                4
   FR@3           n/a         n/a       n/a         n/a      n/a         1        FR@15               n/a      n/a       10           8           6                4
   FR@5             7           6        5            5        4         1        FR@20                19       16       10           8           6                4
  FR@10             7           6        5            5        4         1        AR@1                n/a      n/a       n/a        n/a         n/a              n/a
  FR@15             7           6        5            5        4         1        AR@5                n/a      n/a       n/a        n/a         n/a                4
  FR@20             7           6        5            5        4         1        AR@10               n/a      n/a       10           8           8               7.3
  AR@1            n/a         n/a       n/a         n/a      n/a         1        AR@15               n/a      n/a       12         10.5        9.3               8.5
  AR@3            n/a         n/a       n/a         n/a      n/a         2        AR@20               19.5      18      13.3        13.3         12              10.4
  AR@5            n/a         n/a        5            5        4        3.3        AUC                0.72     0.81     0.82        0.75        0.82              0.9
  AR@10            8.7        7.8       7.8          7.4     7.4        4.7
  AR@15           11.2         10       9.5          10      9.1        7.6
  AR@20           13.3        12.1     12.6         12.1     12.4      10.3           Table 5: RQ1. Method-Level VD on Reveal Dataset
   AUC            0.68        0.72     0.79         0.77     0.79      0.84
                                                                                                    VulDee-   SySeVR   Russell     Devign      Reveal      IVDetect
                                                                                                    -Pecker             et al.
because they did not have correct detections in top-3 results. IVDe-             nDCG@1                 0        0        0           0           0                0
                                                                                 nDCG@3                 0        0        0           0           0              0.63
tect can improve nDCG@10 from 43%–84% and nDCG@20 from                           nDCG@5                 0        0        0           0         0.43             0.53
37%–71% as compared to the baselines. Higher nDCG indicates that                 nDCG@10                0      0.30     0.32        0.34        0.39             0.52
IVDetect achieves the ranking closer to the perfect ranking and                  nDCG@15              0.26     0.28     0.32        0.39        0.42             0.55
                                                                                 nDCG@20              0.27     0.33     0.35        0.43        0.48             0.57
the correct vulnerable methods appear higher in the top list.                     MAP@1                 0        0        0           0           0                0
   For MAP scores, IVDetect relatively improves over the baselines                MAP@3                 0        0        0           0           0              0.33
                                                                                  MAP@5                 0        0        0           0         0.2              0.37
from 105%–255% for top-10 and from 53%–116% for top 20. With                     MAP@10                 0      0.11     0.11        0.18        0.24             0.34
higher MAP, IVDetect has higher precision on average for all the                 MAP@15               0.07     0.12     0.16        0.23        0.25             0.36
top-ranked positions in the top list. That is, the top-ranked result             MAP@20               0.11     0.15     0.18        0.36        0.29             0.37
                                                                                   FR@1               n/a      n/a       n/a        n/a         n/a              n/a
is highly precise in detecting the vulnerable methods.                             FR@3               n/a      n/a       n/a        n/a         n/a                3
   IVDetect also achieves better first ranking (FR) and average                    FR@5               n/a      n/a       n/a        n/a           5                3
ranking (AR). While its best FR is 1 and that of next best performer              FR@10               n/a       10        9           7           5                3
                                                                                  FR@15                15       10        9           7           5                3
is 4. For AR@10, a correct vulnerable method is on average ranked                 FR@20                15       10        9           7           5                3
by IVDetect 2.7–4.0 positions higher in the ranked list than by the               AR@1                n/a      n/a       n/a        n/a         n/a              n/a
baselines. Our tool also has relatively higher AUC from 6%–24%.                   AR@3                n/a      n/a       n/a        n/a         n/a                3
                                                                                  AR@5                n/a      n/a       n/a        n/a           5                4
   The comparative results on Fan and Reveal datasets are similar                 AR@10               n/a       10        9           8           6                6
(Tables 4 and 5). In Fan dataset, IVDetect can improve the nDCG                   AR@15                15      12.5      12         10.5        9.8               9.5
                                                                                  AR@20                18      15.5     13.3        12.7         13              11.8
and MAP scores over the baselines by 26%–43%, 50%–170% for top-                    AUC                0.65     0.76     0.75        0.72        0.74             0.81
10, and 21%–475%, 40%–250% for top-20. IVDetect’s FRs and ARs
are better from 2–6 positions and 0.7–2.7 positions for top 10, and
2–13 positions and 1.6–9.1 positions for top 20. In Reveal dataset,             Table 6: RQ1. Precision and Recall Results of Method-Level
the improvements in nDCG, MAP, FR, and AR are 33%–73%, 42%–                     VD on Three Datasets (P: Precision; R: Recall; F: F score)
209%, 2–7 positions, and 0–4 positions for top 10, and 19%–111%,                                       FFMPeg+Qemu               Fan                    Reveal
28%–236%, 2–12 positions, and 1.2–6.2 positions for top 20.                                            P    R    F       P        R      F       P        R        F
                                                                                  VulDeePecker        0.49 0.27 0.35    0.12     0.49   0.19    0.19     0.14     0.17
   The results on three datasets are different due to the ratio be-                  SySeVR           0.50 0.66 0.56    0.15     0.74   0.27    0.24     0.42     0.31
tween the vulnerable and non-vulnerable methods. That ratio is                     Russell et al.     0.55 0.41 0.45    0.16     0.48   0.24    0.26     0.12     0.16
1:16 and 1:9.9 in Fan and Reveal datasets. That number is 1:1.2 in                   Devign           0.52 0.63 0.57    0.18     0.52   0.26    0.33     0.32     0.32
                                                                                      Reveal          0.55 0.73 0.62    0.19     0.74   0.30    0.31     0.58     0.40
FFMPeg+Qemu dataset, thus, there are more vulnerable methods,                       IVDetect          0.60 0.72 0.65    0.23     0.72   0.35    0.39     0.52     0.45
and the results are consistently higher across all the models.
   Table 6 shows the results of Precision and Recall of our IVDe-
tect and the baselines. Specifically, IVDetect has higher precision             and 2.7%) and SySeVR on Fan dataset (i.e., 2.7%). On the Reveal
than all the baselines on three datasets. IVDetect can improve                  Dataset, IVDetect can improve Reveal by 25.8% in terms of Preci-
the Precision by 2.6%-105%. For the Recall, IVDetect is marginally              sion, but decrease Recall by 10.3%. However, in terms of F1 score,
lower than Reveal on Fan and FFMPeg+Qemu datasets (i.e., 1.4%                   IVDetect can improve the best performed baseline Reveal by 4.8%

## Strona 9

Vulnerability Detection with Fine-Grained Interpretations                                            ESEC/FSE ’21, August 23–28, 2021, Athens, Greece


                                                                          Table 7: RQ2. Fine-grained VD Interpretation Comparison

                                                                          Interp.                     Accuracy
                                                                                                                                      MFR MAR
                                                                          Model N1 N2 N3 N4 N5 N6 N7 N8 N9 N10
                                                                          ATT 0.01 0.16 0.41 0.54 0.59 0.60 0.62 0.63 0.64 0.65 4.8 6.3
                                                                          GRAD 0.01 0.19 0.43 0.54 0.59 0.62 0.63 0.65 0.66 0.67 4.2 5.6
                                                                           GE     0.05 0.30 0.54 0.63 0.67 0.68 0.70 0.72 0.72 0.73 3.5 5.0
                                                                          GE: GNNExplainer; Nx: x is the number of nodes in the interpretation
            (a) MAP Scores                          (b) nDCG Scores

    Figure 7: Scores from Top 1 to Top 100 on Fan Dataset                      Table 8: RQ3. Numbers of Vulnerable Code Patterns

                                                                                                  thres=2 thres=3 thres=4 thres=5
                                                                                      size=2        47      36      22       7
                                                                                      size=3        25      27      19       6
                                                                                      size=4        23      22      16       5
                                                                                      size=5        22      21      11       2
                                                                                       Total        117     102     68      21


                                                                         statement level. That is, in more cases, if IVDetect detects correctly
        (a) nDCG & MAP Scores                        (b) FR and AR       vulnerable methods, it can point out more precisely the vulnerable
                                                                         statements relevant to the vulnerabilities. For ranking vulnerable
Figure 8: RQ1. Cross-Dataset Validation: Training on Reveal
                                                                         statements, using GNNExplainer improves MFR by 0.7 and 1.3 ranks,
and FFMPeg+Qemu Datasets, testing on Fan Dataset.
                                                                         and improves MAR by 0.6 and 1.3 ranks over ATT and GRAD.
                                                                            ATT uses the edge attention in the Graph Attention Network to
                                                                         assign the weights for the edges, while GNNExplainer directly gives
                                                                         a score for the subgraph after masking. Thus, for the case in which
                                                                         there are more than one path from a node to another, the weight
                                                                         for an edge is the average weight of the weights through multiple
                   Figure 9: Overlapping Analysis                        paths, i.e., ATT might be less precise than GNNExplainer. GRAD
                                                                         computes the gradient of the loss function with respect to the input
                                                                         for computing the weight of an edge. However, such gradient-based
on FFMPeg+Qemu dataset, 16.7% on Fan dataset, and 12.5% on the           approach may not perform well with respect to the discrete inputs
Reveal Dataset.                                                          (an input graph is represented as an adjacency matrix).
   Figure 7 shows that IVDetect consistently has better MAP and             As the number of nodes in G𝑀 increases, the number of state-
nDCG scores when considering top-1 to top-100 ranked lists.              ments covered also increases, accuracy is higher. However, the com-
   For cross-dataset validation, as seen in Figure 8, the results for    putation time is higher and developers need to investigate more
MAP and nDCG in within-dataset setting are better than those in          statements. As seen, when the number of statements is higher than
cross-dataset setting. This is expected because the model might see      5, accuracy increases more slowly. Thus, we chose 5 as a default.
similar vulnerable code before in the same projects in the same
dataset. The FR and AR values for cross-dataset setting are one rank     6.3     RQ3. Vulnerable Code Pattern Analysis
higher than those of within-dataset setting.                             This section describes another experiment that we exploit IVDe-
   Figure 9 shows our analysis on the overlapping results between        tect’s capability of providing interpretation sub-graphs to mine the
IVDetect and the baselines on Fan dataset for top-100. As seen,          patterns of vulnerable code. A vulnerable code pattern is a fragment
IVDetect can detect 17, 13, 13, 11, and 10 vulnerable methods            of vulnerable code that repeats frequently, i.e., more than a certain
that VulDeePecker, SySeVR, Russell, Devign, and Reveal missed,           threshold. The detected vulnerability patterns and corresponding
respectively, while they can detect only 2,3, 4, 5, and 5 vulnerable     fixes can be the good sources for developers to learn about the
methods that IVDetect missed. In summary, IVDetect can detect            vulnerable code that others have frequently made, and learn to fix
15, 10, 9, 6, and 5 more vulnerable methods than the baselines.          vulnerable code in the same patterns.
                                                                             From the results in RQ2, we first collected into a set G the inter-
6.2     RQ2. Comparison with other Interpretation                        pretation sub-graphs G𝑀 s with the correctly detected statements
        Models for Fine-grained VD Interpretation                        as relevant to the vulnerability in the methods. In total, we obtain
Table 7 shows the accuracy of different interpretation models. As        +700 G𝑀 s. Note that G𝑀 is a sub-graph of PDG. For each G𝑀 , we
seen, using GNNExplainer improves over ATT and GRAD from                 abstract out the variables’ names with a keyword VAR, and the
12.3%–400% and 9.0%–400% in accuracy, respectively, as we vary           literals with their data types. We then ran the sub-graph pattern
the size of interpretation sub-graphs (i.e., the number of statements)   mining algorithm [24] on G with different thresholds of frequen-
from 1–10. Higher accuracy indicates that IVDetect can provide           cies and collected different sizes of the sub-graph patterns. The
better fine-grained vulnerability detection interpretation at the        outputs are the frequent isomorphic sub-graphs within G𝑀 s, which

### Obrazy na stronie

- `image` obiekt 8: ![image strona 9 obiekt 8](pdfimages/ivdetect/ivdetect-008.png)
- `image` obiekt 9: ![image strona 9 obiekt 9](pdfimages/ivdetect/ivdetect-009.png)
- `image` obiekt 10: ![image strona 9 obiekt 10](pdfimages/ivdetect/ivdetect-010.png)
- `image` obiekt 11: ![image strona 9 obiekt 11](pdfimages/ivdetect/ivdetect-011.png)
- `image` obiekt 12: ![image strona 9 obiekt 12](pdfimages/ivdetect/ivdetect-012.png)
- `smask` obiekt 13: ![smask strona 9 obiekt 13](pdfimages/ivdetect/ivdetect-013.png)

## Strona 10

ESEC/FSE ’21, August 23–28, 2021, Athens, Greece                                                                                                        Li, Wang, and Nguyen


                                                                                            Table 9: RQ4. Evaluation for the Impact of Internal Features.
 1   // ========================PATTERN 1 =======================================
 2       if (is_link(STRINGLITERAL)) {
 3           fprintf(stderr, "Error: invalid /etc/skel/.zshrc file\n"); // not in pattern                      ST     (A)+SST (B)+AST (C)+Var (D)+CD              (E)+DD
 4           exit(INTLITERAL);                                                                                 (A)       (B)        (C)        (D)        (E)         (F)
 5       }
 6       if (copy_file(STRINGLITERAL, VAR) == INTLITERAL) { ...
                                                                                               nDCG@15        0.25      0.27       0.29       0.35        0.42       0.45
 7   // ========================PATTERN 2 =======================================              nDCG@20        0.26      0.27       0.29       0.37        0.44       0.46
 8       VAR = udf_get_filename(VAR, VAR, VAR, VAR);                                            MAP@15        0.07      0.11       0.12       0.19        0.26       0.28
 9           if (VAR && ...) goto LABEL;
                                                                                                MAP@20        0.09      0.11       0.13       0.19        0.26       0.28
                                                                                                 FR@15          14       12          11         7           5          4
                                                                                                 FR@20          14       12          11         7           5          4
                 Figure 10: Vulnerable Code Patterns                                             AR@15          14      13.5         11       10.3          9         8.5
                                                                                                 AR@20        19.5       15        13.5       12.5        11.2       10.4
                                                                                                  AUC         0.75      0.76       0.77       0.83        0.85        0.9
 1   // ===================== FIXING PATTERN 1 =========================
 2   - VAR = fl6_update_dst(VAR, VAR, VAR);                                                 ST: sequence of tokens; SST: sequence of sub-tokens; AST: sub-AST; Var: variables;
 3   + rcu_read_lock();                                                                             CD: control dependencies; DD: data dependencies; F = IVDetect
 4   + final_p = fl6_update_dst(VAR, rcu_dereference(VAR), VAR);
 5   + rcu_read_unlock();
 6   // ===================== FIXING PATTERN 2 =========================
 7   - char VAR = malloc (VAR);
 8   + char VAR;
                                                                                            to cause a denial-of-service (heap-based buffer over-read) or possibly
 9
10
     + if (VAR < 0 || VAR > LITCONST) {
     +   error_line (STRINGLITERAL, VAR);
                                                                                            overwrite the heap via a maliciously crafted DSDIFF file”. This fixing
11   +   return LITCONST;                                                                   pattern occurred three times in the same project.
12   + }
13   + VAR = malloc (VAR);

                                                                                            6.4     RQ4. Sensitivity Analysis for Features
      Figure 11: Fixing Patterns (-: removal, +: addition)                                  Table 9 shows the changes to the metrics as we incrementally added
                                                                                            each internal feature into our model in Figure 4. Generally, each
are considered as vulnerable code patterns because we chose G𝑀                              internal feature contributes positively to the better performance of
that contains correct interpretation statements relevant to the cor-                        IVDetect, as both the score metrics (nDCG, MAP, and AUC) and
rectly detected vulnerabilities. After manual verification, we obtain                       the ranking metrics (FR and AR) are improved.
a number of correct patterns (Table 8). As seen, as the frequency                              When IVDetect considers only the sequence of tokens (ST) in
threshold or the size of pattern is larger, the number of patterns                          the code, the first correct detection (FR) is at the position 14, thus,
decreases as expected. When they are both larger than 5, we found                           nDCG@{1,5,10}=0 and MAP@{1,5,10}=0 (not shown). When consid-
no pattern. Let us explain a few examples.                                                  ering the code as the sequence of sub-tokens (SST), IVDetect deals
    Figure 10 shows two examples of vulnerable code patterns. The                           with the unique tokens better because the sub-tokens appear more
first pattern (lines 2,4, and 6) shows an API misuse in the project                         frequently than the tokens [31]. At top-20, FR improves 2 positions,
firejail involving is_link(...), exit, and copy_file(...). The usage is to check            AR improves 4.5 positions, and nDCG and MAP relatively improve
the validity of a link, and if yes to copy the file, or otherwise to                        3.8% and 22.2%. When AST is additionally considered, the model can
stop the execution. This pattern appeared three times with different                        distinguish vulnerable code structures and statements. At top-20,
string literals and was fixed by developers to replace the statements.                      FR and AR improve 1 and 1.5 positions, and nDCG and MAP im-
An interesting observation is that IVDetect is able to eliminate                            prove 7.4% and 18.1%. However, FR is still 11 and nDCG@{1,5,10}=0
the fprintf statement at line 2 from the interpretation sub-graph,                          and MAP@{1,5,10}=0 (not shown), because tokens and AST do not
thus, eliminating it from the pattern, even though the fprintf state-                       help much discriminate the vulnerable statements.
ment appears with the other statements three times in the project.                             The feature on variables also helps improve FR and AR from 11 to
This shows a benefit of IVDetect because if a tool does not have                            7 and 13.5 to 12.5, and nDCG and MAP relatively improve 27.6% and
statement-level VD interpretation and it mines pattern from the                             46.2% at top 20. nDCG@10 and MAP@10 improve from 0 to 0.33 and
entire methods, it will incorrectly include fprintf in the pattern. The                     to 0.18, respectively (not shown). This feature allows the model to
second pattern (lines 8–9) shows a pattern involving a vulnerable                           detect similar incorrect variable usages. By additionally integrating
method call udf_get_filename, and the checking on its return value.                         control dependencies (CD), FR and AR improve from 7 down to 5
The method later was fixed to add the 5𝑡ℎ parameter.                                        and 12.5 down to 11.2, and nDCG and MAP relatively improve 18.9%
    Another interesting finding is that IVDetect enables the discov-                        and 36.8%. By adding data dependencies (DD), FR and AR improve
ery of not only vulnerable code patterns but also the fixing patterns                       from 5 to 4 and 11.2 to 10.4. nDCG and MAP improve 4.5% and 7.7%
for them. Figure 11 shows two fixing patterns for vulnerable code.                          for top 20. This result confirms that vulnerable code often involves
The first vulnerability (from Linux kernel), lines 2–5, is about the                        the statements with control and/or data dependencies [11, 37].
method f16_update_dst(...). According to the commit log, to avoid an-                          Figure 12 shows a detected vulnerable method: validate_event(...)
other thread changing a data record concurrently, developers need                           was vulnerable and replaced with a new version with an additional
to provide mutual exclusion access and deferencing. This fixing                             parameter. We used the models (A)–(F) for detection, and observed
pattern was repeated 3 times in the methods dccp_v6_send_response,                          that the rank for validate_event(...) in the candidate list improves
inet6_csk_route_req, and net6_csk_route_socket. This fixing pattern                         from 140 (A), to 121 (B), 99 (C), 71 (D), 48 (E), and 19 (F). While the
would be useful for a developer to learn the fix from one method                            features on tokens, sub-tokens, and AST are contributing, they do
and apply to the other two methods. The second pattern (lines 7–13)                         not help much because the model did not see them in vulnerable
shows a fixing pattern to a vulnerability on buffer overflow with                           methods before. However, the variable/method names, especially
the malloc call in ParseDsdiffHeaderConfig method of WavPack 5.0.                           control/data dependencies between the surrounding statements and
According to CVE-2018-7253, this problem “allows a remote attacker                          validate_event(...) help discriminate this vulnerability, and push it to

## Strona 11

Vulnerability Detection with Fine-Grained Interpretations                                                                  ESEC/FSE ’21, August 23–28, 2021, Athens, Greece


                                                                                         been built on top of distinct metrics, such as terms and their occur-
 1   static int validate_group(struct perf_event *event)
 2   {      ...                                                                          rence frequencies [28], imports and function calls [23], complexity,
 3   - if (!validate_event(&fake_pmu, leader))
 4   + if (!validate_event(event->pmu, &fake_pmu, leader))                               code churn, and developer activity [30], dependency relation [22],
 5          return -EINVAL;
 6                                                                                       API symbols and subtrees [34, 35].
 7
 8   -
          list_for_each_entry(sibling, &leader->sibling_list, group_entry) {
              if (!validate_event(&fake_pmu, sibling))
                                                                                            Recently, deep learning (DL) has been applied to detect vulnera-
 9
10
     +        if (!validate_event(event->pmu, &fake_pmu, sibling))
                  return -EINVAL;
                                                                                         bilities. For example, some approaches train a DL model on different
11        }                                                                              code representations to detect vulnerabilities, such as the lexical
12
13   -    if (!validate_event(&fake_pmu, event))                                         representations of functions in a synthetic codebase [14], code snip-
14   +    if (!validate_event(event->pmu, &fake_pmu, event))
15            return -EINVAL; ...                                                        pets related to API calls to detect two types of vulnerabilities [20],
16   }
                                                                                         syntax-based, semantics-based, and vector representations [19],
                                                                                         graph-based representations [37]. None of them is designed to pro-
 Figure 12: A Detected Vulnerable Method in Android kernel                               vide interpretations for a model in term of vulnerable statements.

         Table 10: RQ5. Sensitivity Analysis on Training Data
                                                                                         8     CONCLUSION
         Train/Tune/Test       nDCG@20 MAP@20                  FR@20      AR@20   AUC
         40%/30%/30%             0.26   0.09                     12        15.5   0.69
                                                                                         We present IVDetect, a novel DL-based approach to provide sub-
         50%/25%/25%             0.33   0.16                     8         12.3   0.74   graphs in PDG, that explains the prediction results of graph-based
         60%/20%/20%             0.43   0.25                     5         11.6   0.85   vulnerability detection. Our empirical evaluation on vulnerability
         70%/15%/15%             0.44   0.26                     5         11.2   0.87
         80%/10%/10%             0.46   0.28                     4         10.4   0.9    databases shows that IVDetect outperforms the existing DL-based
                                                                                         approaches by 64%–122% and 105%–255% in top-10 nDCG and MAP
                                                                                         ranking scores.
 the top-20 list. Control dependencies (e.g., between validate_event(...)                   Our key limitations include 1) un-seen vulnerabilities, 2) the
 and return -EINVAL) help improve 29 ranks. Generally, the improve-                      vulnerable statements incorrectly identified due to data/control
 ment in ranking shows the positive contributions of all the features.                   dependencies with vulnerable ones, 3) missed vulnerable statements
    This example also shows a fixing pattern appearing three times                       due to multiple edges of data/control dependencies.
 with different variables leader, sibling, and event.                                       With IVDetect being a ML/DL-based vulnerability detection
                                                                                         model, we aim to raise the level of ML/DL-based approaches, which
 6.5        RQ5. Sensitivity Analysis on Training Data                                   are not able to point out the statements that caused the model to
 As seen in Table 10, with more training data, the performance is                        predict the vulnerability. Thus, we compared IVDetect with the
 better as expected. Even with 60%/20%/20%, IVDetect still achieves                      detection approaches of the same category, rather than with static-
 nCDG of 0.43 and MAP of 0.25, which are still higher than those                         analysis tools. In the future, we plan to compare IVDetect with
 of the other baselines for top 20 (highest nDCG and MAP of the                          static analysis tools.
 baselines are 0.38 and 0.20). With 20% less training data (60% vs
 80%), IVDetect only drops AUC by 5.5%.                                                  ACKNOWLEDGMENTS
 Time Complexity. To generate the interpretation sub-graphs for                          This work was supported in part by the US National Science Foun-
 all methods, it takes about 9 days, 2 days, and 3 days to finish on                     dation (NSF) grants CCF-1723215, CCF-1723432, TWC-1723198,
 Fan, Reveal, and FFMPeg+Qemu datasets, respectively. It took 23,                        CCF-1518897, and CNS-1513263.
 7, 10 hours to train IVDetect on Fan, Reveal, and FFMPeg+Qemu
 datasets. For VD prediction, it takes only 1-2s per method.                             REFERENCES
 Threats to Validity. We only tested on the vulnerabilities in C and                      [1] [n.d.]. Checkmarx. https://www.checkmarx.com/
 C++ code. In principle, IVDetect can apply to other programming                          [2] [n.d.]. Coverity. https://scan.coverity.com/
                                                                                          [3] [n.d.]. CWE-120: Buffer Overflow. https://cwe.mitre.org/data/definitions/120.html
 languages. We tried our best to tune the baselines on same dataset                       [4] [n.d.]. CWE-290: Authentication Bypass by Spoofing. https://cwe.mitre.org/data/
 for fair comparisons. We focus only on DL-based VD models.                                   definitions/290.html
                                                                                          [5] [n.d.]. CWE-79: Cross-site Scripting. http://cwe.mitre.org/data/definitions/79.html
 7        RELATED WORK                                                                    [6] [n.d.]. CWE-89: SQL Injection. https://cwe.mitre.org/data/definitions/89.html
                                                                                          [7] [n.d.]. FlawFinder. http://www.dwheeler.com/FlawFinder
 Various techniques have been developed to detect vulnerabilities.                        [8] [n.d.]. HP Fortify. https://www.hpfod.com/
 The rule-based approaches were developed to leverage known vul-                          [9] [n.d.]. RATS: Rough Audit Tool for Security. https://code.google.com/archive/p/
                                                                                              rough-auditing-tool-for-security/
 nerability patterns to discover possible vulnerable code, such as                       [10] 2021.      The GitHub Repository for This Study.               https://github.com/
 FlawFinder [7], RATS [9], ITS4 [33], Checkmarx [1], Fortify [8]                              vulnerabilitydetection/VulnerabilityDetectionResearch
 and Coverity [2]. Typically, the patterns are manually defined by                       [11] Saikat Chakraborty, Rahul Krishna, Yangruibo Ding, and Baishakhi Ray. 2020.
                                                                                              Deep Learning based Vulnerability Detection: Are We There Yet? arXiv preprint
 human experts. The state-of-the-art vulnerability detection tools                            arXiv:2009.07235 (2020).
 using static analysis provide the rules for each vulnerability type.                    [12] Junyoung Chung, Caglar Gulcehre, KyungHyun Cho, and Yoshua Bengio. 2014.
                                                                                              Empirical evaluation of gated recurrent neural networks on sequence modeling.
    Another type is machine learning (ML)-based or metrics-based.                             arXiv preprint arXiv:1412.3555 (2014).
 Typically, these approaches require the human-crafted or summa-                         [13] Jiahao Fan, Yi Li, Shaohua Wang, and Tien Nguyen. 2020. A C/C++ Code Vulner-
 rized metrics as features to characterize vulnerabilities and train ma-                      ability Dataset with Code Changes and CVE Summaries. In The 2020 International
                                                                                              Conference on Mining Software Repositories (MSR). IEEE.
 chine learning models on the defined features to predict whether a                      [14] Jacob Harer, Onur Ozdemir, Tomo Lazovich, Christopher Reale, Rebecca Russell,
 given code is vulnerable or not. Various ML-based approaches have                            Louis Kim, et al. 2018. Learning to repair software vulnerabilities with generative

## Strona 12

ESEC/FSE ’21, August 23–28, 2021, Athens, Greece                                                                                                          Li, Wang, and Nguyen


     adversarial networks. In Advances in Neural Information Processing Systems. 7933–         international conference on Automated software engineering. 447–456.
     7943.                                                                                [27] Rebecca Russell, Louis Kim, Lei Hamilton, Tomo Lazovich, Jacob Harer, Onur
[15] Jacob A Harer, Louis Y Kim, Rebecca L Russell, Onur Ozdemir, Leonard R Kosta,             Ozdemir, Paul Ellingwood, and Marc McConley. 2018. Automated vulnerability
     Akshay Rangamani, Lei H Hamilton, Gabriel I Centeno, Jonathan R Key, Paul M               detection in source code using deep representation learning. In 2018 17th IEEE
     Ellingwood, et al. 2018. Automated software vulnerability detection with machine          International Conference on Machine Learning and Applications (ICMLA). IEEE,
     learning. arXiv preprint arXiv:1803.04497 (2018).                                         757–762.
[16] Fabian Keller, Lars Grunske, Simon Heiden, Antonio Filieri, Andre van Hoorn,         [28] Riccardo Scandariato, James Walden, Aram Hovsepyan, and Wouter Joosen. 2014.
     and David Lo. 2017. A critical evaluation of spectrum-based fault localization            Predicting vulnerable software components via text mining. IEEE Transactions
     techniques on a large-scale software system. In 2017 IEEE International Conference        on Software Engineering 40, 10 (2014), 993–1006.
     on Software Quality, Reliability and Security (QRS). IEEE, 114–125.                  [29] Min Shi, Yufei Tang, Xingquan Zhu, and Jianxun Liu. 2019. Feature-attention
[17] Thomas N. Kipf and Max Welling. 2016. Semi-Supervised Classification with                 graph convolutional networks for noise resilient learning. arXiv preprint
     Graph Convolutional Networks. CoRR abs/1609.02907 (2016). arXiv:1609.02907                arXiv:1912.11755 (2019).
     http://arxiv.org/abs/1609.02907                                                      [30] Yonghee Shin, Andrew Meneely, Laurie Williams, and Jason A Osborne. 2010.
[18] Yi Li, Shaohua Wang, Tien N Nguyen, and Son Van Nguyen. 2019. Improving bug               Evaluating complexity, code churn, and developer activity metrics as indicators
     detection via context-based code representation learning and attention-based              of software vulnerabilities. IEEE transactions on software engineering 37, 6 (2010),
     neural networks. Proceedings of the ACM on Programming Languages 3, OOPSLA                772–787.
     (2019), 1–30.                                                                        [31] Trinh Le Son Nguyen, Hung Dang Phan and Tien N. Nguyen. 2020. Suggesting
[19] Zhen Li, Deqing Zou, Shouhuai Xu, Hai Jin, Yawei Zhu, and Zhaoxuan Chen. 2018.            Natural Method Names to Check Name Consistencies. In Proceedings of the 42nd
     Sysevr: A framework for using deep learning to detect software vulnerabilities.           International Conference on Software Engineering (ICSE ’20). ACM Press, 12 pages.
     arXiv preprint arXiv:1807.06756 (2018).                                              [32] Kai Sheng Tai, Richard Socher, and Christopher D Manning. 2015. Improved
[20] Zhen Li, Deqing Zou, Shouhuai Xu, Xinyu Ou, Hai Jin, Sujuan Wang, Zhijun                  semantic representations from tree-structured long short-term memory networks.
     Deng, and Yuyi Zhong. 2018. Vuldeepecker: A deep learning-based system for                arXiv preprint arXiv:1503.00075 (2015).
     vulnerability detection. arXiv preprint arXiv:1801.01681 (2018).                     [33] John Viega, Jon-Thomas Bloch, Yoshi Kohno, and Gary McGraw. 2000. ITS4:
[21] Microsoft. [n.d.]. Neural Network Intelligence. https://github.com/microsoft/nni.         A static vulnerability scanner for C and C++ code. In Proceedings 16th Annual
     Last Accessed August 28th, 2020.                                                          Computer Security Applications Conference (ACSAC’00). IEEE, 257–267.
[22] Stephan Neuhaus and Thomas Zimmermann. 2009. The Beauty and the Beast:               [34] Fabian Yamaguchi, Felix Lindner, and Konrad Rieck. 2011. Vulnerability extrapola-
     Vulnerabilities in Red Hat’s Packages.. In USENIX Annual Technical Conference.            tion: Assisted discovery of vulnerabilities using machine learning. In Proceedings
[23] Stephan Neuhaus, Thomas Zimmermann, Christian Holler, and Andreas Zeller.                 of the 5th USENIX conference on Offensive technologies. 13–13.
     2007. Predicting vulnerable software components. In Proceedings of the 14th ACM      [35] Fabian Yamaguchi, Markus Lottmann, and Konrad Rieck. 2012. Generalized
     conference on Computer and communications security. 529–540.                              vulnerability extrapolation using abstract syntax trees. In Proceedings of the 28th
[24] Tung Thanh Nguyen, Hoan Anh Nguyen, Nam H. Pham, Jafar M. Al-Kofahi, and                  Annual Computer Security Applications Conference. 359–368.
     Tien N. Nguyen. 2009. Graph-Based Mining of Multiple Object Usage Patterns. In       [36] Zhitao Ying, Dylan Bourgeois, Jiaxuan You, Marinka Zitnik, and Jure Leskovec.
     Proceedings of the 7th Joint Meeting of the European Software Engineering Confer-         2019. GNNExplainer: Generating Explanations for Graph Neural Networks. In
     ence and the ACM SIGSOFT Symposium on The Foundations of Software Engineering             Advances in Neural Information Processing Systems 32, H. Wallach, H. Larochelle,
     (Amsterdam, The Netherlands) (ESEC/FSE ’09). Association for Computing Ma-                A. Beygelzimer, F. d'Alché-Buc, E. Fox, and R. Garnett (Eds.). Curran Associates,
     chinery, New York, NY, USA, 383–392. https://doi.org/10.1145/1595696.1595767              Inc., 9244–9255.
[25] Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014. GloVe:         [37] Yaqin Zhou, Shangqing Liu, Jingkai Siow, Xiaoning Du, and Yang Liu. 2019.
     Global Vectors for Word Representation. In Empirical Methods in Natural Lan-              Devign: Effective vulnerability identification by learning comprehensive program
     guage Processing (EMNLP). 1532–1543. http://www.aclweb.org/anthology/D14-                 semantics via graph neural networks. In Advances in Neural Information Processing
     1162                                                                                      Systems. 10197–10207.
[26] Nam H Pham, Tung Thanh Nguyen, Hoan Anh Nguyen, and Tien N Nguyen. 2010.
     Detection of recurring software vulnerabilities. In Proceedings of the IEEE/ACM

## Strona 13

