# vuldeepecker

Źródło: `vuldeepecker.pdf`

## Strona 1

VulDeePecker: A Deep Learning-Based System for
                                                      Vulnerability Detection

                                                                            Zhen Li∗† , Deqing Zou∗‡] , Shouhuai Xu§ , Xinyu Ou∗ , Hai Jin∗ ,
                                                                                   Sujuan Wang∗ , Zhijun Deng∗ and Yuyi Zhong∗
                                                             ∗ Services Computing Technology and System Lab, Big Data Technology and System Lab,

                                                                        Cluster and Grid Computing Lab, School of Computer Science and Technology,
                                                                                       Huazhong University of Science and Technology
                                                                                                    deqingzou@hust.edu.cn
                                                                                  † School of Cyber Security and Computer, Hebei University




arXiv:1801.01681v1 [cs.CR] 5 Jan 2018
                                                                        ‡ Shenzhen Huazhong University of Science and Technology Research Institute
                                                                            § Department of Computer Science, University of Texas at San Antonio


                                            Abstract—The automatic detection of software vulnerabilities        that the number of vulnerabilities registered in the Common
                                        is an important research problem. However, existing solutions to        Vulnerabilities and Exposures (CVE) was approximately 4,600
                                        this problem rely on human experts to define features and often         in 2010, and grew to approximately 6,500 in 2016 [4]. An
                                        miss many vulnerabilities (i.e., incurring high false negative rate).   alternate approach is to automatically detect vulnerabilities in
                                        In this paper, we initiate the study of using deep learning-based       software programs, or simply programs for short. There have
                                        vulnerability detection to relieve human experts from the tedious
                                        and subjective task of manually defining features. Since deep
                                                                                                                been many static vulnerability detection systems and studies
                                        learning is motivated to deal with problems that are very different     for this purpose, ranging from open source tools [6], [11],
                                        from the problem of vulnerability detection, we need some guiding       [52], to commercial tools [2], [3], [7], to academic research
                                        principles for applying deep learning to vulnerability detection. In    projects [19], [28], [32], [37], [38], [49], [59], [60]. However,
                                        particular, we need to find representations of software programs        existing solutions for detecting vulnerabilities have two major
                                        that are suitable for deep learning. For this purpose, we propose       drawbacks: imposing intense manual labor and incurring high
                                        using code gadgets to represent programs and then transform             false negative rates, which are elaborated below.
                                        them into vectors, where a code gadget is a number of (not
                                        necessarily consecutive) lines of code that are semantically related        On one hand, existing solutions for vulnerability detection
                                        to each other. This leads to the design and implementation              rely on human experts to define features. Even for experts,
                                        of a deep learning-based vulnerability detection system, called         this is a tedious, subjective, and sometimes error-prone task
                                        Vulnerability Deep Pecker (VulDeePecker). In order to evaluate          because of the complexity of the problem. In other words,
                                        VulDeePecker, we present the first vulnerability dataset for deep       the identification of features is largely an art, meaning that the
                                        learning approaches. Experimental results show that VulDeeP-            quality of the resulting features, and therefore the effectiveness
                                        ecker can achieve much fewer false negatives (with reasonable           of resulting detection system, varies with the individuals who
                                        false positives) than other approaches. We further apply VulDeeP-
                                                                                                                define them. In principle, this problem can be alleviated by
                                        ecker to 3 software products (namely Xen, Seamonkey, and
                                        Libav) and detect 4 vulnerabilities, which are not reported in          asking multiple experts to define their own features, and then
                                        the National Vulnerability Database but were “silently” patched         select the set of features that lead to better effectiveness or use
                                        by the vendors when releasing later versions of these products;         a combination of these features. However, this imposes even
                                        in contrast, these vulnerabilities are almost entirely missed by        more tedious work. As a matter of fact, it is always desirable
                                        the other vulnerability detection systems we experimented with.         to reduce, or even eliminate whenever possible, the reliance
                                                                                                                on the intense labor of human experts. This can be justified
                                                                   I.    I NTRODUCTION                          by the trend of cyber defense automation, which is catalyzed
                                                                                                                by initiatives such as DARPA’s Cyber Grand Challenge [5].
                                            Many cyber attacks are rooted in software vulnerabilities.          It is therefore important to relieve human experts from the
                                        Despite the effort that has been invested in pursuing secure pro-       tedious and subjective task of manually defining features for
                                        gramming, software vulnerabilities remain, and will continue,           vulnerability detection.
                                        to be a significant problem. This can be justified by the fact
                                                                                                                    On the other hand, existing solutions often miss many
                                          ] Corresponding author                                                vulnerabilities or incur high false negative rates. For example,
                                                                                                                two most recent vulnerability detection systems, VUDDY [28]
                                                                                                                and VulPecker [32], respectively incur a false negative rate
                                                                                                                of 18.2% (when detecting vulnerabilities of Apache HTTPD
                                        Network and Distributed Systems Security (NDSS) Symposium 2018          2.4.23) and 38% (when applied to 455 vulnerability samples).
                                        18-21 February 2018, San Diego, CA, USA                                 Our own independent experiments show that they respectively
                                        ISBN 1-1891562-49-5                                                     incur a false negative rate of 95.1% and 89.8% (see Table
                                        http://dx.doi.org/10.14722/ndss.2018.23158                              V in Section IV). Note that the large discrepancy between
                                        www.ndss-symposium.org
                                                                                                                the false negative rates reported in [28], [32] and the false
                                                                                                                negative rates derived from our experiments is caused by the

## Strona 2

use of different datasets. These high false negative rates may                  a vulnerability detection system that can detect only
be justified by their emphasis on low false positive rates,                     one type of vulnerabilities would be too limited. Ex-
which are respectively 0% for VUDDY [28] and unreported                         perimental results answer this question affirmatively.
for VulPecker [32]. Our independent experiments show that                       This can be explained by the fact that VulDeePecker
their false positive rates are respectively 0% for VUDDY and                    uses vulnerability patterns (learned as deep neural
1.9% for VulPecker (see Table V in Section IV). This suggests                   networks) to detect vulnerabilities.
that VUDDY and VulPecker are designed to achieve low false
positive rates, which appear to be inherent to the approach of            •     Can human expertise help improve the effectiveness of
detecting vulnerabilities caused by code clones; in contrast,                   VulDeePecker? Experimental results show that the ef-
when using this approach to detecting vulnerabilities that are                  fectiveness of VulDeePecker can be further improved
not caused by code clones, high false negative rates occur.                     by incorporating human expertise, which is not for
                                                                                defining features though. This hints that automatic
    It would be fair to say that vulnerability detection systems                vulnerability detection systems, while being able to re-
with high false positive rates may not be usable, vulnerability                 lieve human experts from the tedious labor of defining
detection systems with high false negative rates may not be                     features, may still need to leverage human expertise
useful. This justifies the importance of pursuing vulnerability                 from other purposes. This poses an important open
detection systems that can achieve low false negative rates and                 problem for future study.
low false positive rates. When this cannot be achieved (because
false positive and false negative are often at odds with each             •     How effective is VulDeePecker when compared with
                                                                                other vulnerability detection approaches? Experimen-
other), we may put emphasis on lowering the false negative
                                                                                tal results show that VulDeePecker is much more
rate as long as the false positive rate is not too high.
                                                                                effective than the other static analysis tools, which
    The aforementioned two limitations of existing solutions                    ask human experts to define rules for detecting vul-
motivate the importance of designing the vulnerability detec-                   nerabilities, and the state-of-the-art code similarity-
tion system without asking human experts to manually define                     based vulnerability detection systems (i.e., VUDDY
features and without incurring high false negative rate or false                and VulPecker).
positive rate. In this paper, we propose a solution to the
following vulnerability detection problem while bearing in                These questions may be seen as an initial effort at defining
mind with these limitations: Given the source code of a target         a benchmark for evaluating the effectiveness of deep learning-
program, how can we determine whether or not the target                based vulnerability detection systems.
program is vulnerable and if so, where are the vulnerabilities?            In order to show the usefulness of VulDeePecker, we fur-
                                                                       ther apply it to 3 software products (namely Xen, Seamonkey,
Our contributions. The present paper represents a first step           and Libav). VulDeePecker is able to detect 4 vulnerabilities,
towards ultimately tackling the aforesaid problem. Specifically,       which are not reported in the National Vulnerability Database
we make three contributions.                                           (NVD) [10] but were “silently” patched by the vendors when
    First, we initiate the study of using deep learning for            releasing later versions of these products. In contrast, these
vulnerability detection. This approach has a great potential           vulnerabilities are almost entirely missed by the other vulnera-
because deep learning does not need human experts to man-              bility detection systems we experimented with. More precisely,
ually define features, meaning that vulnerability detection can        one of those vulnerability detection systems is able to detect 1
be automated. However, this approach is challenging because            of the 4 vulnerabilities (i.e., missing 3 of the 4 vulnerabilities),
deep learning is not invented for this kind of applications,           while the other systems missed all of the 4 vulnerabilities.
meaning that we need some guiding principles for applying              We will conduct more experiments to show whether or not
deep learning to vulnerability detection. We discuss some              VulDeePecker can detect vulnerabilities that have not been
preliminary guiding principles for this purpose, including the         identified, including possibly 0-day vulnerabilities.
representation of software programs to make deep learning                  Third, since there are no readily available datasets for
suitable for vulnerability detection, the determination of gran-       answering the questions mentioned above, we present the first
ularity at which deep learning-based vulnerability detection           dataset for evaluating VulDeePecker and other deep learning-
should be conducted, and the selection of specific neural              based vulnerability detection systems that will be developed in
networks for vulnerability detection. In particular, we propose        the future. The dataset is derived from two data sources main-
using code gadgets to represent programs. A code gadget is             tained by the National Institute of Standards and Technology
a number of (not necessarily consecutive) lines of code that           (NIST): the NVD [10] and the Software Assurance Reference
are semantically related to each other, and can be vectorized          Dataset (SARD) project [12]. The dataset contains 61,638 code
as input to deep learning.                                             gadgets, including 17,725 code gadgets that are vulnerable
    Second, we present the design and implementation of                and 43,913 code gadgets that are not vulnerable. Among the
a deep learning-based vulnerability detection system, called           17,725 code gadgets that are vulnerable, 10,440 code gadgets
Vulnerability Deep Pecker (VulDeePecker). We evaluate the ef-          correspond to buffer error vulnerabilities (CWE-119) and the
fectiveness of VulDeePecker from the following perspectives:           rest 7,285 code gadgets correspond to resource management
                                                                       error vulnerabilities (CWE-399). We have made the dataset
   •    Can VulDeePecker deal with multiple types of vul-              available at https://github.com/CGCL-codes/VulDeePecker.
        nerabilities at the same time? This perspective is
        important because a target program in question may             Paper organization. The rest of the paper is organized as
        contain multiple types of vulnerabilities, meaning that        follows. Section II presents some preliminary guiding prin-

                                                                   2

## Strona 3

ciples for deep learning-based vulnerability detection. Section        finer granularity than treating a program or a function as a
III discusses the design of VulDeePecker. Section IV describes         unit.
our experimental evaluation of VulDeePecker and results.
Section V discusses the limitations of VulDeePecker and open               Indeed, the aforementioned code gadget representation
problems for future research. Section VI describes the related         leads to a fine-grained granularity for vulnerability detection
prior work. Section VII concludes the present paper.                   because a code gadget often consists of a small number of
                                                                       lines of code. This means that the code gadget representation
                                                                       naturally satisfies Guiding Principle 2.
 II.   G UIDING P RINCIPLES FOR D EEP L EARNING -BASED
               V ULNERABILITY D ETECTION                               C. How to select neural networks?
    In this section, we propose some preliminary guiding                   Neural networks have been very successful in areas such
principles for using deep learning to detect vulnerabilities.          as image processing, speech recognition, and natural language
These principles are sufficient for the present study, but may         processing (e.g., [21], [30], [40]), which are different from
need to be refined to serve the more general purpose of deep           vulnerability detection. This means that many neural networks
learning-based vulnerability detection. These principles are           may not be suitable for vulnerability detection, and that we
centered at answering three fundamental questions: (i) How             need some principles to guide the selection of neural networks
to represent programs for deep learning-based vulnerability            that are suitable for vulnerability detection. Our examination
detection? (ii) What is the appropriate granularity for deep           suggests the following:
learning-based vulnerability detection? (iii) How to select a
specific neural network for vulnerability detection?                       Guiding Principle 3: Because whether or not a line of
                                                                       code contains a vulnerability may depend on the context,
                                                                       neural networks that can cope with contexts may be suitable
A. How to represent software programs?                                 for vulnerability detection.
    Since deep learning or neural networks take vectors as                 This principle suggests that neural networks for natural
input, we need to represent programs as vectors that are               language processing may be suitable for vulnerability detection
semantically meaningful for vulnerability detection. In other          because context is also important in natural language pro-
words, we need to encode programs into vectors that are                cessing [33]. Putting the notion of context into the setting
the required input for deep learning. Note that we cannot              of the present paper, we observe that the argument(s) of a
arbitrarily transform a program into vectors because the vectors       program function call is often affected by earlier operations in
need to preserve the semantic information of the program.              the program and may also be affected by later operations in
This suggests us to use some intermediate representation as            the program.
a “bridge” between a program and its vector representation,
which is the actual input to deep learning. This leads to the              Since there are many neural networks for natural lan-
following:                                                             guage processing, let us start with Recurrent Neural Networks
                                                                       (RNNs) [51], [53]. These neural networks are effective in
    Guiding Principle 1: Programs can be first transformed             coping with sequential data, and indeed have been used for
into some intermediate representation that can preserve (some          program analysis (but not for vulnerability detection purposes)
of) the semantic relationships between the programs’ elements          [20], [48], [56], [57]. However, RNNs suffer from the Vanish-
(e.g., data dependency and control dependency). Then, the              ing Gradient (VG) problem, which can cause ineffective model
intermediate representation can be transformed into a vector           training [16]. Note that the VG problem is inherited by the
representation that is the actual input to neural networks.            Bidirectional variant of RNNs, called BRNNs [47]. We would
    As we will elaborate later, Guiding Principle 1 leads us to        prefer neural networks that do not suffer from the VG problem.
propose an intermediate representation dubbed code gadget.                 The VG problem can be addressed with the idea of memory
The term code gadget is inspired by the term of gadget in the          cells into RNNs, including the Long Short-Term Memory
context of code-reuse attacks (see, e.g., [18]), because a code        (LSTM) cell and the Gated Recurrent Unit (GRU) cell [17],
gadget is a small number of (not necessarily consecutive) lines        [22]. Since the GRU does not outperform the LSTM on
of code.                                                               language modeling [27], we select LSTM for vulnerability
                                                                       detection and defer its comparison with GRU to future work.
B. What is an appropriate granularity?                                 However, even LSTM may be insufficient for vulnerability
                                                                       detection because it is unidirectional (i.e., from earlier LSTM
    Since it is desirable not only to detect whether a program         cells to later LSTM cells). This is because the argument(s) of a
is vulnerable or not, but also to pin down the locations of            program function call may be affected by earlier statements in
the vulnerabilities, a finer granularity should be used for            the program and may be also affected by the later statements.
deep learning-based vulnerability detection. This means that           This suggests that unidirectional LSTM may be insufficient
vulnerability detection should not be conducted at the program         and that we should use Bidirectional LSTM (BLSTM) for
or function level, which are too coarse-grained because a              vulnerability detection.
program or function may have many lines of code and pinning
down the locations of its vulnerability can be a difficult task            Figure 1 highlights the structure of BLSTM neural network,
by itself. This leads to:                                              which has a number of BLSTM layers, a dense layer, and
                                                                       a softmax layer. The input to the learning process is in a
    Guiding Principle 2: In order to help pin down the loca-           certain vector representation. The BLSTM layers have two
tions of vulnerabilities, programs should be represented at a          directions, forward and backward. The BLSTM layers contain

                                                                   3

## Strona 4

some complex LSTM cells, which are treated as black-boxes in               calls, the key points are the library/API function calls; for
the present paper and therefore deferred to Appendix A. The                vulnerabilities that are caused by improper uses of arrays, the
dense layer reduces the number of dimensions of the vectors                key points are the arrays. It is important to note that a type
received from the BLSTM layers. The softmax layer takes                    of vulnerabilities may have multiple kinds of key points. For
the low-dimension vectors received from the dense layer as                 example, buffer error vulnerabilities may correspond to the
input, and is responsible for representing and formatting the              following key points: library/API function calls, arrays, and
classification result, which provides feedback for updating the            pointers. Moreover, the same kind of key points may exist in
neural network parameters in the learning phase. The output                multiple types of vulnerabilities. For example, both buffer error
of the learning phase is a BLSTM neural network with fine-                 and resource management error vulnerabilities may contain
tuned model parameters, and the output of the detection phase              the key points of library/API function calls. Precisely defining
is the classification results.                                             the heuristic concept of key point is beyond the scope of the
                                                                           present paper and is left as an interesting problem for future
                         Output: learned BLSTM with parameters/            research; instead, we focus on using this heuristic concept as
                                   classification results                  the “lens” to use deep learning to learn vulnerability patterns.
       Softmax layer                      .. .
                                                                               In this paper, we focus on using the particular key point of
                                                                           library/API function calls to demonstrate its usefulness in deep
                                                  .. .
       Dense layer                                                         learning-based vulnerability detection. This is motivated by the
                                                                           observation that many vulnerabilities are related to library/API
                                            ...
                        LSTM     LSTM                    LSTM   LSTM       function calls. It is also an interesting future work to investigate
                                                                           the usefulness of other kinds of key points.
       BLSTM layers       ...     ...                     ...    ...

                                                                               Corresponding to the key point of library/API function
                                          ...
                        LSTM     LSTM                    LSTM   LSTM       calls, code gadgets can be generated by the means of data flow
                                                                           or control flow analysis of program, for which there are well
            Vectors
                                          .. .                             known algorithms [23], [50] and readily usable commercial
                         ...      ...                     ...    ...
                                                                           products such as Checkmarx [2]. It is worth mentioning that
                                                                           Checkmarx also detects vulnerabilities based on some rules
Figure 1.    A brief review of BLSTM neural network                        that are manually defined by human experts. However, we do
                                                                           not use its rules for vulnerability detection; instead, we will
                                                                           compare the effectiveness of VulDeePecker against it.
                 III.   D ESIGN OF V UL D EE P ECKER
    Our objective is to design a vulnerability detection system            B. Overview of VulDeePecker
that can automatically tell whether a given program in source                  As highlighted in Figure 2, VulDeePecker has two phases:
code is vulnerable or not and if so, the locations of the                  a learning (i.e., training) phase and a detection phase. The
vulnerabilities. This should be achieved without asking human              input to the learning phase is a large number of training
experts to manually define features and without incurring                  programs, some of which are vulnerable and the others are
high false negative rates (as long as the false positive rates             not. By “vulnerable” we mean that a program contains one
are reasonable). In this section, we describe the design of                or multiple known vulnerabilities. The output of the learning
VulDeePecker. We start with a discussion on the notion of code             phase is vulnerability patterns, which are coded into a BLSTM
gadget, because it is crucial to the representation of programs.           neural network.
Then, we give an overview of VulDeePecker and elaborate its
components.                                                                    1) The learning phase: As highlighted in Figure 2(a), the
                                                                           learning phase has 4 steps.
A. Defining code gadget                                                    Step I: Extracting the library/API function calls and the
    In order to represent programs in vectors that are suitable            corresponding program slices. This has two sub-steps, which
for the input to neural networks, we first propose transforming            are highlighted below and elaborated in Section III-C.
programs into a representation of code gadget, which is defined
as follows:                                                                   •     Step I.1: Extracting library/API function calls from
                                                                                    the training programs, while noting that the current
    Definition 1: (Code gadget) A code gadget is composed of                        version of VulDeePecker focuses on vulnerabilities
a number of program statements (i.e., lines of code), which are                     related to the key point of library/API function calls.
semantically related to each other in terms of data dependency
or control dependency.                                                        •     Step I.2: Extracting one or multiple program slices for
                                                                                    each argument (or variable) of a library/API function
    In order to generate code gadgets, we propose the heuristic                     call that is extracted in Step I.1. In this paper, a
concept of key point, which can be seen as a “lens” through                         program slice represents the statements of a program
which we can represent programs from a certain perspective.                         (i.e., lines of code) that are semantically related to
Intuitively, the heuristic concept of key point can be seen as,                     an argument of a library/API function call, while
in a sense, the “center” of a vulnerability or the piece of code                    noting that the notion of program slice was originally
that hints the existence of a vulnerability. For vulnerabilities                    introduced to represent the statements of a program
that are caused by improper uses of library/API function                            with respect to a program point or variable [55].

                                                                       4

## Strona 5

Input        Step I: Extracting library/API Step II: Generating code                      Step III: Transforming code                          Step IV: Training BLSTM                            Output
                          function calls and the     gadgets and their ground                         gadgets into vectors                                  neural network
                      corresponding program slices          truth labels
                         from training programs
                             Step I.1: Extracting              Step II.1:                           Step III.1: Transforming                 Softmax                      ...
      Training              library/API function             Assembling                                code gadgets into                       layer
     programs              calls from the training      program    slices into                     symbolic representations                  Dense                                ...                     BLSTM neural
        (i.e.,                     programs                 code gadgets                                                                      layer                                                       network with
     software                                                                                                                                           LSTM      LSTM     ...
                                                                                                                                                                                        LSTM      LSTM     fine-tuned
     programs                                                                                    Step III.2: Encoding the                                                                                     model
                                                                                                                                             BLSTM
    for training                                                                               symbolic representations of                   layers      ...       ...                   ...       ...
                                                                                                                                                                                                           parameters
        deep                                                    Step II.2: Each code
                                                                 gadget is labeled              code gadgets into vectors
      learning              Step I.2: Extracting                                                                                                       LSTM       LSTM    ...
                                                                                                                                                                                        LSTM      LSTM

                              program slices                       as “1” or “0”                The symbolic
       neural                                                                                 representation of
     networks)            corresponding to the                    Code gadget    Label       the ith code gadget                                      [ vi1       vi2    ...            vi(τ-1)   viτ ]
                             arguments of the                    Code gadget 1     1           Token Vector        Vector of symbolic
                        library/API function calls               Code gadget 2     0            main      vi1       representation
                                                                 Code gadget 3     1               (      vi2
                                                                 Code gadget 4     0                                [vi1,vi2, …, viτ]
                                                                                                 int      vi3
                                                                 Code gadget 5     0            argc      vi4
                                                                      ...          ...            ...     ...


                                                                                          (a) Learning phase

         Input                                     Step V: Transforming target programs into code gadgets and vectors                                                            Step VI: Detection             Output

         Target        Step V.1: Extracting     Step V.2: Extracting                                 Step V.4: Transforming              Step V.5: Encoding              Step VI: Applying the trained
                       library/API function        program slices        Step V.3: Assembling                                                the symbolic                  BLSTM neural network to
        programs                                                          program slices into          code gadgets into
                       calls from the target     corresponding to                                           symbolic                       representations                classify the code gadgets of
                              programs           the function calls          code gadgets                                                     into vectors                 target programs in vector
                                                                          (similar to Step II.1)         representations
                        (similar to Step I.1)   (similar to Step I.2)                                 (similar to Step III.1)           (similar to Step III.2)                  representation              Code gadgets
    Trained BLSTM                                                                                                                                                                                            are vulnerable
    neural network                                                                                                                                                                                               or not
    with fine-tuned
        model
      parameters

                                                                                         (b) Detection phase

Figure 2. Overview of VulDeePecker: the learning phase generates vulnerability patterns, and the detection phase uses these vulnerability patterns to determine
whether a target program is vulnerable or not and if so, the locations of the vulnerabilities (i.e., the corresponding code gadgets).


Step II: Generating code gadgets of the training programs                                                  Step IV: Training a BLSTM neural network. Having en-
and their ground truth labels. This step has two sub-steps,                                                coded the code gadgets into vectors and obtained their ground
which are highlighted below and elaborated in Section III-D.                                               truth labels, the training process for learning a BLSTM neural
                                                                                                           network is standard.
    •      Step II.1: Assembling the program slices obtained
           in Step I.2 into code gadgets, one code gadget per                                                  2) The detection phase: Given one or multiple target
           library/API function call. A code gadget does not                                               programs, we extract library/API function calls from them as
           necessarily correspond to some consecutive lines of                                             well as the corresponding program slices, which are assembled
           code. Instead, it consists of multiple lines of code that                                       into code gadgets. The code gadgets are transformed into
           are semantically related to each other (i.e., inheriting                                        their symbolic representations, which are encoded into vectors
           the semantic relation that is encoded in those program                                          and used as input to the trained BLSTM neural network.
           slices).                                                                                        The network outputs which vectors, and therefore which code
                                                                                                           gadgets, are vulnerable (“1”) or not (“0”). If a code gadget is
    •      Step II.2: Labeling the ground truth of code gadgets.                                           vulnerable, it pins down the location of the vulnerability in the
           This step labels each code gadget as “1” (i.e., vulner-                                         target program. As highlighted in Figure 2(b), this phase has
           able) or “0” (i.e., not vulnerable). The ground truth                                           two steps.
           labels of code gadgets are available because we know                                            Step V: Transforming target programs into code gadgets
           whether a training program is vulnerable or not and                                             and vectors. It has five sub-steps.
           if it is vulnerable, we also know the locations of the
           vulnerabilities.                                                                                        •       Step V.1: Extracting library/API function calls from
                                                                                                                           the target programs (similar to Step I.1).
Step III: Transforming code gadgets into vector represen-
tations. This step has two sub-steps, which are highlighted                                                        •       Step V.2: Extracting program slices according to the
below and elaborated in Section III-E.                                                                                     arguments of the library/API function calls (similar to
                                                                                                                           Step I.2).
    •      Step III.1: Transforming code gadgets into certain                                                      •       Step V.3: Assembling the program slices into code
           symbolic representations, which will be elaborated                                                              gadgets (similar to Step II.1).
           later. This step aims to preserve some semantic in-
           formation of the training programs.                                                                     •       Step V.4: Transforming the code gadgets to their
                                                                                                                           symbolic representations (similar to Step III.1).
    •      Step III.2: Encoding code gadgets in the symbolic rep-                                                  •       Step V.5: Encoding the symbolic representations of
           resentation obtained in Step III.1 into vectors, which                                                          code gadgets into vectors (similar to Step III.2).
           are the input for training a BLSTM neural network.
           This is necessary in order to use neural networks in                                            Step VI: Detection. This step uses the learned BLSTM neural
           general.                                                                                        network to classify the vectors corresponding to the code

                                                                                                       5

### Obrazy na stronie

- `image` obiekt 0: ![image strona 5 obiekt 0](pdfimages/vuldeepecker/vuldeepecker-000.png)

## Strona 6

1 void
     2 test(char *str)                                                                        13
     3 {                                                                                                    The backward function call strcpy has two arguments,
     4 int MAXSIZE=40;                                                                             str      buf and str, each of which leads to a backward slice.
     5 char buf[MAXSIZE];
     6                                                                                                      The slice corresponding to buf consists of statements
                                                                                              15            belong ing to the user-defined function test (indicated
     7 if(!buf)
     8      return;                                                                              str main() by a dashed rectangle).
     9 strcpy(buf, str); /*string copy*/                                                                    The slice corresponding to str consists of statements
     10 }                                                                     test()          18            scattered in two user-defined functions, main and
     11                                                                                                     test, which are also indicated by dashed rectangles.
     12 int                                                                                      str
     13 main(int argc, char **argv)                                             4
     14 {                                           Backward                                  19
     15 char *userstr;                             fu nction call                   buf                              13 main(int argc, char **argv)
     16                                                                                            str               15 char *userstr;
     17 if(argc > 1) {                                                                                                                                     main()
                                                 9 strcpy(buf, str);            5                                    18 userstr = argv[1];
     18       userstr = argv[1];                                                              2                      19 test(userstr);
     19       test(userstr);                     /*string copy*/
                                                                                    buf                              2 test(char *str)
     20   }                                                                                        str test()        4 int MAXSIZE=40;                     test()
     21   return 0;                                                                                                  5 char buf[MAXSIZE];
     22 }                                                                       9             9                      9 strcpy(buf, str); /*string copy*/

                                               Step I.1: Extracting            Step I.2: Generating                   Step II.1 Assembling slices
          Program source code                 library/API function            slices of arguments in                      into code gadgets
                                                       calls                library/API function calls

Figure 3. Illustrating the extraction of library/API function calls (Step I.1) from a (training) program, which contains a backward function call (i.e., strcpy)
that is also used as an example to demonstrate the extraction of program slices (Step I.2) and the assembly of program slices into code gadgets (Step II.1).


gadgets that are extracted from the target programs. When a                             2) Step I.2: Extracting program slices: This step gener-
vector is classified as “1” (i.e., vulnerable), it means that the                   ates program slices corresponding to the arguments of the
corresponding code gadget is vulnerable and the location of                         library/API function calls that are extracted from the training
the vulnerability is pinned down. Otherwise, the corresponding                      programs. We define two kinds of slices: forward slices and
code gadget is classified as “0” (i.e., not vulnerable).                            backward slices, where a forward slice corresponds to the
                                                                                    statements that are affected by the argument in question and a
    Steps I-III are respectively elaborated in the following                        backward slice corresponds to the statements that can affect the
subsections. Steps IV and VI are standard and Step V is similar                     argument in question. We take advantage of the commercial
to some of Steps I-III.                                                             product Checkmarx [2], more specifically its data dependency
                                                                                    graph, to extract these two kinds of slices. The basic idea is
C. Step I: Extracting library/API function calls and program                        the following:
slices
    1) Step I.1: Extracting library/API function calls: We                                •    For each argument in a forward library/API function
classify library/API function calls into two categories: forward                               call, one or multiple forward slices are generated,
library/API function calls and backward library/API function                                   with the latter corresponding to the case that the slice
calls. Forward library/API function calls are the function calls                               related to the argument is branched at, or after, the
that receive one or multiple inputs directly from the external                                 library/API function call.
input, such as the command line, a program, a socket, or a file.                          •    For each argument in a backward library/API function
For example, the recv function call is a forward library/API                                   call, one or multiple backward slices are generated,
function call because it receives data from a socket directly.                                 with the latter corresponding to the case that multiple
Backward library/API function calls are the function calls that                                slices related to the argument are merged at, or prior
do not receive any external input directly from the environment                                to, the library/API function call.
in which the program runs.
    Figure 3 shows an example of a backward library/API                                 Note that a program slice consists of multiple statements
function call strcpy (line 9). It is a backward library/API                         that may belong to multiple user-defined functions. That is, a
function call because it does not receive any external input                        slice can go beyond the boundary of user-defined functions in
directly.                                                                           question.
    We highlight a distinction between forward and backward                             Figure 3 shows an example program that contains the
library/API function calls. For forward library/API function                        library function call strcpy, which has two arguments buf and
calls, the statements influenced by the input arguments are crit-                   str. Since strcpy is a backward function call, for each of its
ical because they may be vulnerable to improper (e.g., sophis-                      arguments we will generate a backward slice. For argument
ticatedly crafted) argument values; for backward library/API                        buf , the slice consists of three statements, namely lines 4,
function calls, the statements influencing the values of the                        5, and 9 of the program, which belong to the user-defined
arguments are critical because they could make the library/API                      function test. For argument str, the slice consists of six
function calls vulnerable. This insight will be leveraged to                        statements, namely lines 13, 15, 18, 19, 2, and 9 of the
guide the heuristic padding of the vector representations of                        program, where the first 4 belong to the user-defined function
code gadgets.                                                                       main and the last 2 belong to the user-defined function test.

                                                                               6

## Strona 7

The two slices are chains (i.e., a linear structure) because             Second, map user-defined variables to symbolic names (e.g.,
Checkmarx uses chains to represent slices, while noting that             “VAR1”, “VAR2”) in the one-to-one fashion, while noting that
slices can also be represented by trees [23], [50]. Since the            multiple variables may be mapped to the same symbolic name
linear structure can only represent one individual slice, a              when they appear in different code gadgets. Third, map user-
library/API function call often corresponds to multiple slices.          defined functions to symbolic names (e.g., “FUN1”, “FUN2”)
                                                                         in the one-to-one fashion, while noting that multiple functions
D. Step II: Extracting code gadgets and labeling their ground            may be mapped to the same symbolic name when they appear
truth                                                                    in different code gadgets.
    1) Step II.1: Assembling program slices into code gadgets:              13 main(int argc, char **argv)        13 main(int argc, char **argv)
The program slices generated in the previous step can be                    15 ch ar *userstr;                    15 ch ar *userstr;
assembled into code gadgets as follows.                                     18 userstr = argv[1];                 18 userstr = argv[1];
                                                                            19 test(userstr);                     19 test(userstr);
                                                                            2 test(char *str)                     2 test(char *str)
    First, given a library/API function call and the correspond-            4 int MAXSIZE=40;                     4 int MAXSIZE=40;
ing program slices, we combine the statements (i.e., pieces of              5 ch ar buf[MAX SIZE];                5 char buf[MAXSIZE];
                                                                            9 strcpy(buf, str); /*string copy*/   9 strcpy(buf, str);
code) belonging to the same, user-defined function into a single                                                     (1) Remove non-ASCII
                                                                          Inp ut: code gadget (from Step II.1)
piece according to the order of the statements’ appearance                                                         characters and comments
in the user-defined function. If there is a duplication of any
statement, the duplication is eliminated.                                   13 main(int argc, char **argv)        13 main(int argc, ch ar **argv)
                                                                            15 char *VAR1;                        15 char *VAR1;
    In the example shown in Figure 3, three statements (i.e.,               18 VAR1 = argv[1];                    18 VAR1 = argv[1];
                                                                            19 test(VAR1);                        19 FUN1(VAR1);
lines 4, 5, and 9) belonging to the user-defined function test              2 test(ch ar *VAR2)                   2 FUN1(char *VAR2)
consists the program slice corresponding to the argument buf ,              4 int VAR3=40;                        4 int VAR3=40;
                                                                            5 ch ar VAR4[VAR3];                   5 ch ar VAR4[VAR3];
and two statements (i.e., lines 2 and 9) belonging to the                   9 strcpy(VAR5, VAR2);                 9 strcpy(VAR5, VAR2);
user-defined function test are a piece of the program slice                 (2) Map user-defined variables        (3) Map user-defined functions
corresponding to the argument str. Therefore, we need to
assemble them into a single piece because they are related to            Figure 4. Illustration of Step III.1: transforming code gadgets into their
the same function test. According to the line numbers of these           symbolic representations
statements’ appearance in the function test, this would lead to
2 → 4 → 5 → 9 → 9. Since the statement corresponding                         Figure 4 highlights the above process by using the code
to line 9 is duplicated, we eliminate the duplication to derive          fragment generated by Step II.1 as shown in Figure 3.
a piece of assembled statements 2 → 4 → 5 → 9, which                         2) Step III.2: Encoding the symbolic representations into
correspond to the function test.                                         vectors: Each code gadget needs to be encoded into a vector
    Second, assembling the statements belonging to different,            via its symbolic representation. For this purpose, we divide
user-defined functions into a single code gadget. If there is            a code gadget in the symbolic representation into a sequence
already an order between two pieces of statements belonging to           of tokens via lexical analysis, including identifiers, keywords,
these user-defined functions, this order is preserved; otherwise,        operators, and symbols. For example, a code gadget in the
a random order is used.                                                  symbolic representation,
    In the example shown in Figure 3, when assembling the                                         “strcpy(VAR5, VAR2); ”
piece of statements belonging to the user-defined function               is represented by a sequence of 7 tokens:
main (i.e., lines 13, 15, 18, and 19) and the assembled piece of
statements belonging to user-defined function test (i.e., lines                  “strcpy”, “(”, “VAR5”, “,”, “VAR2”, “)”, and “;”.
2, 4, 5, and 9), we obtain 13 → 15 → 18 → 19 → 2 → 4 →
                                                                         This leads to a large corpus of tokens. In order to transform
5 → 9, which is a code gadget corresponding to the library
                                                                         these tokens into vectors, we use the word2vec tool [14], which
function call strcpy. This code gadget preserves the order of
                                                                         is selected because it is widely used in text mining [58]. This
user-defined functions that are contained in the program slice
                                                                         tool is based on the idea of distributed representation, which
corresponding to the argument str.
                                                                         maps a token to an integer that is then converted to a fixed-
    2) Step II.2: Labeling the ground truth: Each code gadget            length vector [43].
needs to be labeled as “1” (i.e., vulnerable) and “0” (i.e., not
                                                                             Since code gadgets may have different numbers of tokens,
vulnerable). If a code gadget corresponds to a vulnerability that
                                                                         the corresponding vectors may have different lengths. Since
is known in the training dataset, it is labeled as “1”; otherwise,
                                                                         BLSTM takes equal-length vectors as input, we need to make
it is labeled as “0”. In Section IV-C, we will discuss the
                                                                         an adjustment. For this purpose, we introduce a parameter τ
labeling of ground truth in details, when dealing with programs
                                                                         as the fixed length of vectors corresponding to code gadgets.
related to specific vulnerability data sources.
                                                                             •      When a vector is shorter than τ , there are two cases: if
E. Step III: Transforming code gadgets into vectors                                 the code gadget is generated from a backward slice or
                                                                                    generated by combining multiple backward slices, we
    1) Step III.1: Transforming code gadgets into their sym-
                                                                                    pad zeros in the beginning of the vector; otherwise,
bolic representations: This step aims to heuristically capture
                                                                                    we pad zeros to the end of the vector.
some semantic information in the programs for training a
neural network. First, remove the non-ASCII characters and                   •      When a vector is longer than τ , there are also two
comments because they have nothing to do with vulnerability.                        cases: if the code gadget is generated from one

                                                                     7

## Strona 8

·T P R
        backward slice, or generated by combining multiple               F 1-measure metric F 1 = 2·P   P +T P R takes consideration of
        backward slices, we delete the beginning part of the             both precision and true positive rate.
        vector; otherwise, we delete the ending part of the
                                                                             It would be ideal that a vulnerability detection system
        vector.
                                                                         neither misses vulnerabilities (i.e., F N R ≈ 0 and T P R ≈ 1)
    This ensures that the last statement of every code gadget            nor triggers false alarms (i.e., F P R ≈ 0 and P ≈ 1), which
generated from a backward slice is a library/API function call,          means F 1 ≈ 1. However, this is difficult to achieve in practice,
and that the first statement of every code gadget generated              and often forces one to trade the effectiveness in terms of one
from a forward slice is a library/API function call. As a result,        metric for the effectiveness in terms of another metric. In this
every code gadget is represented as a τ -bit vector. The length          study, we prefer to achieving low FNR and low FPR.
of vectors is related to the number of hidden nodes at each
layer of the BLSTM, which is a parameter that can be tuned               B. Preparing input to VulDeePecker
to improve the accuracy of vulnerability detection (see Section          Collecting programs. There are two widely used sources of
IV-C).                                                                   vulnerability data maintained by the NIST: the NVD [10]
                                                                         which contains vulnerabilities in production software, and
             IV.   E XPERIMENTS AND R ESULTS                             the SARD project [12] which contains production, synthetic,
                                                                         and academic security flaws or vulnerabilities. In the NVD,
    Our experiments are centered at answering the following              each vulnerability has a unique Common Vulnerabilities and
three research questions (RQs):                                          Exposures IDentifier (CVE ID) and a Common Weakness
                                                                         Enumeration IDentifier (CWE ID) that indicates the type of
   •    RQ1: Can VulDeePecker deal with multiple types of                the vulnerability in question. We collect the programs that
        vulnerabilities at the same time?                                contain one or multiple vulnerabilities. In the SARD, each
        A vulnerability detection system should be able to               program (i.e., test case) corresponds to one or multiple CWE
        detect multiple types of vulnerabilities at the same             IDs because a program can have multiple types of vulnerabil-
        time, because multiple detection systems need to be              ities. Therefore, programs with one or multiple CWE IDs are
        maintained otherwise. For answering this question, we            collected.
        will conduct experiments involving one or multiple
        types of vulnerabilities.                                            In the present paper, we focus on two types of vulnerabil-
                                                                         ities: buffer error (i.e., CWE-119) and resource management
   •    RQ2: Can human expertise (other than defining fea-               error (i.e., CWE-399), each of which has multiple subtypes.
        tures) improve the effectiveness of VulDeePecker?                These vulnerabilities are very common, meaning that we can
        For answering this question, we will investigate the             collect enough data for using deep learning. We select 19
        effectiveness of using some manually-selected li-                popular C/C++ open source products, including the Linux
        brary/API function calls vs. the effectiveness of using          kernel, Firefox, Thunderbird, Seamonkey, Firefox esr, Thun-
        all of the library/API function calls.                           derbird esr, Wireshark, FFmpeg, Apache Http Server, Xen,
   •    RQ3: How effective is VulDeePecker when compared                 OpenSSL, Qemu, Libav, Asterisk, Cups, Freetype, Gnutls,
        with other vulnerability detection approaches?                   Libvirt, and VLC media player, which contain, according to
        For answering this question, we will compare                     the NVD, these two types of vulnerabilities. We also collect
        VulDeePecker with other approaches, including some               the C/C++ programs in the SARD that contain these two
        static analysis tools and code similarity-based vulner-          types of vulnerabilities. In total, we collect from the NVD
        ability detection systems.                                       520 open source software programs related to buffer error
                                                                         vulnerabilities and 320 open source software programs related
                                                                         to resource management error vulnerabilities; we also collect
A. Metrics for evaluating vulnerability detection systems                from the SARD 8,122 programs (i.e., test cases) related to
                                                                         buffer error vulnerabilities and 1,729 programs related to
    We use the widely used metrics false positive rate (F P R),
                                                                         resource management error vulnerabilities. Note that program
false negative rate (F N R), true positive rate or recall (T P R),
                                                                         containing a vulnerability may actually consist of multiple
precision (P ), and F 1-measure (F 1) to evaluate vulnerabil-
                                                                         program files.
ity detection systems [39]. Let TP be the number of samples
with vulnerabilities detected correctly, FP be the number of             Training programs vs. target programs. We randomly
samples with false vulnerabilities detected, FN be the number            choose 80% of the programs we collect as training programs
of samples with true vulnerabilities undetected, and TN be               and the remaining 20% as target programs. This ratio is applied
the number of samples with no vulnerabilities undetected.                equally when dealing with one or both types of vulnerabilities.
                                              FP
The false positive rate metric F P R = FP+TN        measures the
ratio of false positive vulnerabilities to the entire population         C. Learning BLSTM neural networks
of samples that are not vulnerable. The false negative rate
                     FN                                                     This corresponds to the learning phase of VulDeePecker.
metric F N R = TP+FN      measures the ratio of false negative
                                                                         We implement the BLSTM neural network in Python using
vulnerabilities to the entire population of samples that are
                                                                         Theano [24] together with Keras [8]. We run experiments on
vulnerable. The true positive rate or recall metric T P R =
   TP                                                                    a machine with NVIDIA GeForce GTX 1080 GPU and Intel
TP+FN measures the ratio of true positive vulnerabilities to the         Xeon E5-1620 CPU operating at 3.50GHz.
entire population of samples that are vulnerable, while noting
                                                             TP
that T P R = 1 − F N R. The precision metric P = TP+FP                   Step I: Extracting library/API function calls and cor-
measures the correctness of the detected vulnerabilities. The            responding program slices. We extract C/C++ library/API

                                                                     8

## Strona 9

Table I.   DATASETS FOR ANSWERING THE RQ S
function calls from the programs. There are 6,045 C/C++
library/API function calls that involve standard library function                   Dataset
                                                                                              #Code     #Vulnerable    #Not vulnerable
                                                                                              gadgets   code gadgets    code gadgets
calls [1], basic Windows API and Linux kernel API function                         BE-ALL     39,753       10,440          29,313
calls [9], [13]. In total, we extract 56,902 library/API function                  RM-ALL     21,885       7,285           14,600
calls from the programs, including 7,255 forward function calls                    HY-ALL     61,638       17,725          43,913
and 49,647 backward function calls.                                                BE-SEL     26,720       8,119           18,601
                                                                                   RM-SEL     16,198       6,573            9,625
    In order to answer the RQs, we also manually select 124                        HY-SEL     42,918       14,692          28,226
C/C++ library/API function calls (including function calls with
wildcard) related to buffer error vulnerabilities (CWE-119)
and 16 C/C++ library/API function calls related to resource             of the NVD, we focus on the vulnerabilities whose patches
management error vulnerabilities (CWE-399). These function              involve line deletions or modifications. This process has two
calls are selected because the aforementioned commercial                steps. In the first step, a code gadget is automatically labeled
tool Checkmarx [2] claims, using their own rules written by             as “1” (i.e., vulnerable) if it contains at least one statement that
human experts, that they are related to these two types of              is deleted or modified according to the patch, and labeled as
vulnerabilities. The list of these function calls are deferred          “0” otherwise (i.e., not vulnerable). However, this automatic
to Table VII in the Appendix B. Correspondingly, we extract             process may mislabel some code gadgets, which are not
40,351 library/API function calls from the training programs,           vulnerable, as “1”. In order to remove these mislabels, the
including 4,012 forward function calls and 36,339 backward              second step is to manually check the code gadgets that are
function calls. For each argument of the library/API function           labeled as “1” so as to correct the mislabels (if any).
calls, one or multiple program slices are extracted.
                                                                             Recall that each program in the SARD is already labeled
Step II.1: Generating code gadgets. Code gadgets are gener-             as good (i.e., no security defect), bad (i.e., containing security
ated from program slices. We obtain a Code Gadget Database              defects), or mixed (i.e., containing functions with security
(CGD) of 61,638 code gadgets, among which 48,744 code                   defects and their patched versions) with corresponding CWE
gadgets are generated from program slices of training pro-              IDs. For the code gadgets extracted from the programs with
grams, and 12,894 code gadgets are generated from program               respect to the SARD, a code gadget extracted from a good
slices of target programs. The time complexity for generating           program is labeled as “0” (i.e., not vulnerable), and a code
gadgets mainly depends on the data flow analysis tool. For              gadget extracted from a bad or mixed program is labeled as “1”
example, it takes 883 seconds to generate 2,494 code gadgets            (i.e., vulnerable) if it contains at least one vulnerable statement
from 100 programs (99,232 lines) that are randomly selected             and “0” otherwise. Since we used heuristics in the labeling
the SARD, meaning an average of 354 milliseconds per code               process for the SARD program, we looked at the labels of
gadget. For answering the RQs mentioned above, we use the               1,000 random code gadgets and found that only 6 of them (i.e.
CGD to derive the following 6 datasets.                                 0.6%) were mislabeled. These mislabeled samples are caused
                                                                        by the fact that a statement in a piece of code that is not
   •    BE-ALL: The subset of CGD corresponding to Buffer               vulnerable is the same as a statement in a piece of code that
        Error vulnerabilities (CWE-119) and ALL library/API             is vulnerable. As the mislabeled code gadgets are very few
        function calls (i.e., extracted without human expert).          and the neural networks are robust against a small portion of
   •    RM-ALL: The subset of CGD corresponding to Re-                  mislabeled samples, it is unnecessary to check manually all
        source Management error vulnerabilities (CWE-399)               labels of the code gadgets that are extracted for the SARD
        and ALL library/API function calls.                             programs.
   •    HY-ALL: The subset of CGD corresponding to the                      It is possible to encounter the situation that the same code
        HYbrid of (i.e., both) buffer error vulnerabilities             gadget is labeled with both “1” and “0” (i.e., conflicting labels).
        (CWE-119) and resource management error vulner-                 One cause of this phenomenon is the imperfection of the data
        abilities (CWE-399) and ALL library/API function                flow analysis tool. In this case, we simply delete these code
        calls. That is, it is the same as the CGD.                      gadgets. As a result, 17,725 code gadgets are labeled as “1”
   •    BE-SEL: The subset of CGD corresponding to Buffer               and 43,913 code gadgets are labeled as “0”. Among the 17,725
        Error vulnerabilities (CWE-119) and manually SE-                code gadgets labeled as “1”, 10,440 code gadgets correspond
        Lected function calls (rather than all function calls).         to the buffer error vulnerabilities and 7,285 code gadgets
                                                                        correspond to the resource management error vulnerabilities.
   •    RM-SEL: The subset of CGD corresponding to Re-                  Table I shows the number of code gadgets that are vulnerable
        source Management error vulnerabilities (CWE-399)               (Column 3) and the number of code gadgets that are not
        and manually SELected function calls.                           vulnerable in each dataset (Column 4).
   •    HY-SEL: The subset of CGD corresponding to the                  Step III: Transforming code gadgets into vectors. The CGD
        HYbrid of buffer error vulnerabilities (CWE-119) and            contains a total number of 6,166,401 tokens, of which 23,464
        resource management error vulnerabilities (CWE-399)             are different. After mapping user-defined variable names and
        and manually SELected function calls.                           function names to some symbolic names, the number of
    Table I summarizes the number of code gadgets in these              different tokens is further reduced to 10,480. These symbolic
datasets.                                                               representations are encoded into vectors, which are used as the
                                                                        input for training a BLSTM neural network.
Step II.2: Labeling code gadgets. Code gadgets are labeled
as follows. For the code gadgets extracted from the programs            Step IV: Training BLSTM neural network. For each dataset

                                                                    9

## Strona 10

described in Table I, we adopt a 10-fold cross validation to                                              calls that are related to resource management error vulnera-
train a BLSTM neural network, and select the best parameter                                               bilities (i.e., 16) is far smaller than the number of library/API
values corresponding to the effectiveness for vulnerability                                               function calls that are related to buffer error vulnerabilities
detection. For example, we vary the number of hidden layers                                               (i.e., 124). We also observe that, in terms of the FPR and P
for each BLSTM neural network and observe the influence                                                   metrics, the neural network trained from the HY-ALL dataset
on the resulting F1-measure. When we adjust the number of                                                 is not as good as the neural network trained from the BE-ALL
hidden layers, we set the parameters to their default values                                              or RM-ALL dataset. We further observe that the TPR and
when such default values are available, and set the parameters                                            FNR of the neural network trained from the HY-ALL dataset
to the values that are widely used by the deep learning                                                   reside in between that of the neural network trained from the
community otherwise. The number of tokens in the vector                                                   RM-ALL dataset and that of the neural network trained from
representation of code gadgets is set to 50, the dropout is set                                           the BE-ALL dataset. The F1-measure of the neural network
to 0.5, the batch size is set to 64, the number of epochs is set                                          trained from the HY-ALL dataset is 1.2% lower than that
to 4, the minibatch stochastic gradient descent together with                                             of the neural network trained from the BE-ALL dataset, and
ADAMAX [29] is used for training with the default learning                                                9.6% lower than that of the neural network trained from the
rate of 1.0, and 300 hidden nodes are chosen.                                                             RM-ALL dataset. This can be explained by the fact that the
                                                                                                          number of library/API function calls that are related to the
           1 0 0                                                                                          vulnerabilities of the hybrid dataset (i.e., 140) is larger than
                                                                                                          the number of library/API function calls that are related to a
               8 0                                                                                        single type of vulnerabilities. We speculate this is caused by the
                                                                                                          following: it is more difficult to extract vulnerability patterns
                                                                                                          for a large number of library/API function calls that are related
               6 0
                                                                                                          to vulnerabilities than to extract vulnerability patterns for a
    F 1 (% )
                                                                                                          small number of library/API function calls that are related to
               4 0                   F 1 (B E -S E L )
                                                                                                          vulnerabilities.
                                      F 1 (B E -A L L )
                                       F 1 (R M -S E L )                                                      Table III summarizes the training time and detection time
                                        F 1 (R M -A L L )
               2 0                       F 1 (H Y -S E L )
                                                                                                          corresponding to the HY-ALL dataset, where the second col-
                                          F 1 (H Y -A L L )                                               umn represents the number of code gadgets for training (i.e.,
                                                                                                          extracted from the training programs) and the third column
                     0
                         0       5                            1 0              1 5           2 0
                                                                                                          represents the number of code gadgets for detection (i.e.,
                                              N u m b e r o f h id d e n la y e r s
                                                                                                          extracted from the target programs). We observe that the
                                                                                                          training time of VulDeePecker, as implied by the deep learning
Figure 5. F1-measure of VulDeePecker for the 6 datasets with different                                    technology in general, is large, but the detecting time is small.
number of hidden layers
                                                                                                              Table III.     T IME COMPLEXITY OF TRAINING AND DETECTION

    Figure 5 plots the F1-measure of VulDeePecker with re-                                                        Dataset
                                                                                                                              #Training        #Detection    Training   Detection
spect to the 6 datasets with different number of hidden layers,                                                              code gadgets     code gadgets   time (s)   time (s)
                                                                                                                 HY-ALL         48,744           12,894      36,372.2     156.2
each of which leads to a different neural network. We observe
                                                                                                                 HY-SEL         33,813            9,105      25,242.3      76.6
that the F1-measure of the 6 BLSTM neural networks reaches
the maximum at 2 or 3 layers, and the F1-measure of most of
                                                                                                              In summary, we answer RQ1 affirmatively with the follow-
these BLSTM neural networks declines when the number of
                                                                                                          ing:
layers is greater than 6. Note that the other parameters of the
BLSTM neural network can be tuned in a similar fashion.                                                       Insight 1: VulDeePecker can simultaneously detect multi-
                                                                                                          ple types of vulnerabilities, but the effectiveness is sensitive to
                                                                                                          the number of library/API function calls related to vulnerabil-
D. Experimental results & implications
                                                                                                          ities (i.e., the fewer the better).
   1) Experiments for answering RQ1: In order to test                                                         2) Experiments for answering RQ2: In order to answer
whether VulDeePecker can be applied to multiple types of                                                  whether VulDeePecker can be improved by incorporating hu-
vulnerabilities, we conduct experiments on three datasets: BE-                                            man expertise, we conduct the experiment using all library/API
ALL, RM-ALL, and HY-ALL. This respectively leads to three                                                 function calls that are automatically extracted vs. using some
neural networks, whose effectiveness is reported in Table II.                                             library/API function calls that are manually selected under the
    Table II.    R ESULTS FOR ANSWERING RQ1, INDICATING THAT
                                                                                                          guidance of vulnerability rules written by Checkmarx’s human
 V UL D EE P ECKER CAN DETECT MULTIPLE TYPES OF VULNERABILITIES .                                         experts.
            Dataset          FPR(%)               FNR(%)            TPR(%)            P(%)   F1(%)         Table IV. R ESULTS FOR ANSWERING RQ2, INDICATING THAT USING
           BE-ALL              2.9                 18.0              82.0             91.7    86.6          MANUALLY- SELECTED LIBRARY /API FUNCTION CALLS CAN INDEED
           RM-ALL              2.8                  4.7              95.3             94.6    95.0               IMPROVE THE EFFECTIVENESS OF V UL D EE P ECKER .
           HY-ALL              5.1                 16.1              83.9             86.9    85.4
                                                                                                                   Dataset    FPR(%)        FNR(%)     TPR(%)    P(%)    F1(%)
                                                                                                                   HY-ALL       5.1          16.1       83.9     86.9     85.4
   We observe that the neural network trained from the RM-                                                         HY-SEL       4.9           6.1       93.9     91.9     92.9
ALL dataset outperforms the neural network trained from the
BE-ALL dataset in terms of all five metrics. This can be                                                      As shown in Table IV, the BLSTM network trained from
explained by the fact that the number of library/API function                                             the HY-SEL dataset is more effective than the BLSTM network

                                                                                                     10

## Strona 11

Table V.    R ESULTS FOR ANSWERING RQ3: V UL D EE P ECKER ACHIEVES
trained from the HY-ALL dataset. Although the improvement                     A MUCH SMALLER OVERALL FNR OF 7.0% CORRESPONDING TO THE
in FPR is small (0.2%), the improvement in each of the other                ENTIRE BE-SEL DATASET ( THE LARGER FNR OF 16.9% CORRESPONDING
metrics is substantial: 10% in FNR and TPR, 5% in precision,                    TO THE SMALL SUB - DATASET DERIVED FROM THE NVD AND THE
and 7.5% in F1-measure. Moreover, Table III shows that the                  SMALLER FNR OF 5.1% CORRESPONDING TO THE SUB - DATASET DERIVED
                                                                             FROM THE SARD), WHILE NOTING THAT THE OVERALL FPR OF 5.7% IS
training time of using manually selected library/API function               REASONABLY SMALL . “N/C” MEANS THAT THE SYSTEM IS N OT C APABLE
calls can be smaller than that of using all library/API function              OF DETECTING VULNERABILITIES IN THE CORRESPONDING DATASET.
calls, because a smaller number of code gadgets need to be
                                                                                                                    FPR     FNR       TPR       P       F1
processed. This leads to the following preliminary understand-                     System            Dataset
                                                                                                                    (%)     (%)       (%)      (%)     (%)
ing regards the usefulness of human expertise in improving the                     VulDeePecker vs. Other pattern-based vulnerability detection systems
effectiveness of deep learning-based vulnerability detection:                    Flawfinder        BE-SEL           44.7    69.0      31.0     25.0    27.7
                                                                                   RATS            BE-SEL           42.2    78.9      21.1     19.4    20.2
    Insight 2: Human expertise can be used to select li-                         Checkmarx         BE-SEL           43.1    41.1      58.9     39.6    47.3
                                                                                VulDeePecker       BE-SEL            5.7     7.0      93.0     88.1    90.5
brary/API function calls to improve the effectiveness of
                                                                                  VulDeePecker vs. Code similarity-based vulnerability detection systems
VulDeePecker, especially the overall effectiveness in F1-                         VUDDY         BE-SEL-NVD            0     95.1      4.9      100     9.3
measure.                                                                         VulPecker      BE-SEL-NVD           1.9    89.8      10.2     84.3    18.2
                                                                                VulDeePecker    BE-SEL-NVD          22.9    16.9      83.1     78.6    80.8
    3) Experiments for answering RQ3: In order to answer                          VUDDY          BE-SEL-SARD         N/C     N/C      N/C     N/C     N/C
RQ3, we compare the effectiveness of VulDeePecker with                           VulPecker       BE-SEL-SARD         N/C     N/C      N/C     N/C     N/C
                                                                                VulDeePecker     BE-SEL-SARD         3.4     5.1      94.9    92.0    93.4
other pattern-based and code similarity-based vulnerability
detection systems. We here report the comparison between
their effectiveness in detecting buffer error vulnerabilities (i.e.,
BE-SEL dataset), while noting that a similar phenomenon                     system can be more effective by taking advantage of the data
is observed when comparing their effectiveness in detect-                   flow analysis. (This hints us to speculate that a system can be
ing resource management error vulnerabilities (i.e., RM-SEL                 even more effective by taking advantage of the control flow
dataset) — the details are omitted due to the lack of space.                analysis. It is an interesting future work to validate or invalidate
                                                                            this speculation.)
    For comparison with other pattern-based vulnerability de-
tection systems, which use rules defined by human experts,                       Second, for the BE-SEL-NVD sub-dataset, VUDDY and
we consider a commercial product called Checkmarx [2] and                   VulPecker trade high FNRs (95.1% and 89.8%, respectively)
two open source tools called Flawfinder [6] and RATS [11].                  for low FPRs (0% and 1.9%, respectively), which lead to very
These systems are chosen because we have access to them                     low F1-measures (9.3% and 18.2%, respectively). The large
and to the best of our knowledge, they have been widely                     FNRs can explained by the following facts: VUDDY can only
used. For comparison with code similarity-based vulnerability               detect the vulnerabilities related to functions, which are nearly
detection systems, which are mainly geared towards clone-                   identical to the vulnerable functions in the training programs
caused vulnerabilities, we consider the two state-of-the-art                (i.e., vulnerabilities caused by Types I and II code clones [42]);
systems called VUDDY [28] and VulPecker [32]. We use                        VulPecker can only detect vulnerabilities caused by Type I,
VUDDY’s open service, and use the original implementation                   Type II, and some Type III code clones [42] (e.g., deletion,
of VulPecker provided to us by its authors. For fair comparison,            insertion, and rearrangement of statements), which explains
we need to address some subtle issues. We observe that                      why VulPecker incurs a lower FNR than VUDDY. However,
VulPecker uses diffs as an input, where a diff describes the                these systems cannot detect vulnerabilities that are not caused
difference between a vulnerable piece of code and its patched               by code clones, which explains why they incur high FNRs.
version, we divide the BE-SEL dataset of target programs
                                                                                 In contrast, VulDeePecker has a much higher F1-measure
into two subsets, namely BE-SEL-NVD (266 samples derived
                                                                            (i.e., 80.8% vs. 9.3% for VUDDY and 18.2% for VulPecker)
from the NVD) and BE-SEL-SARD (the rest samples derived
                                                                            because it has a much higher TPR (i.e., much lower FNR),
from the SARD). We use BE-SEL-NVD for the comparison
                                                                            while noting that its FPR is 22.9% (vs. 0% for VUDDY and
study because VUDDY and VulPecker were designed to detect
                                                                            1.9% for VulPecker). We suspect that this high FPR of 22.9%
vulnerabilities with CVE IDs or vulnerabilities with diffs, but
                                                                            corresponding to the BE-SEL-NVD dataset is caused by a
are unable to detect vulnerabilities in BE-SEL-SARD.
                                                                            small number of training code gadgets from NVD. This can
    Table V summarizes the comparison. We make the fol-                     be justified by the small FPR of 3.4% corresponding to a large
lowing observations. First, VulDeePecker substantially outper-              number of training code gadgets from SARD, which is about
forms the other pattern-based vulnerability detection systems,              18 times larger than the number of training code gadgets from
because VulDeePecker incurs a FPR of 5.7% and a FNR                         NVD. Moreover, the FPR of 5.7% corresponding to the entire
of 7.0%, which are respectively much smaller than their                     BE-SEL dataset resides some where in between them. The
counterparts in the other detection systems. By looking into                high FNR of 16.9% can be explained similarly.
the other systems, we find that Flawfinder and RATS do not
use data flow analysis and therefore miss many vulnerabilities.                 The high FPR and FNR of VulDeePecker with respect to
Although Checkmarx does use data flow analysis, its rules for               the BE-SEL-NVD sub-dataset should not be used as evidence
recognizing vulnerabilities are defined by human experts and                against VulDeePecker, simply because for the BE-SEL-SARD
are far from perfect. This further highlights the importance of             sub-dataset, VulDeePecker incurs an even smaller FPR of 3.4%
relieving human experts from tedious tasks (similar to task of              and a FNR of 5.1%, while noting that VUDDY and VulPecker
manually defining features). This observation leads to:                     are not applicable (i.e., not capable of detecting vulnerabilities
                                                                            in this sub-dataset). Moreover, VulDeePecker incurs a FPR of
   Insight 3: A deep learning-based vulnerability detection                 5.7% and a FNR of 7.0% over the entire BE-SEL dataset,

                                                                       11

## Strona 12

Table VI. V UL D EE P ECKER DETECTED 4 VULNERABILITIES IN 3 PRODUCTS , WHICH ARE NOT PUBLISHED IN THE NVD BUT HAVE BEEN “ SILENTLY ”
     PATCHED BY THE VENDORS IN THE LATER RELEASES OF THESE PRODUCTS .T HESE VULNERABILITIES ARE ENTIRELY MISSED BY THE OTHER
    VULNERABILITY DETECTION SYSTEMS , EXCEPT THAT F LAW F INDER DETECTED ONLY ONE VULNERABILITY WHILE MISSING THE OTHER THREE .

                                               Vulnerable product    Vulnerability                                         Library/API      1st patched version
             Target product        CVE ID                                             Vulnerable file in target product
                                              published in the NVD   publish time                                          function call     of target product
               Xen 4.6.0      CVE-2016-9104           Qemu            12/09/2016       .../qemu-xen/hw/9pfs/virtio-9p.c      memcpy              Xen 4.9.0
              Seamonkey       CVE-2015-4517          Firefox          09/24/2015      .../system/gonk/NetworkUtils.cpp        snprintf       Seamonkey 2.38
                 2.31         CVE-2015-4513          Firefox          11/05/2015      .../protocol/http/Http2Stream.cpp       memset         Seamonkey 2.39
              Libav 10.2      CVE-2014-2263          FFmpeg           02/28/2014            libavformat/mpegtsenc.c        strchr, strlen       Libav 10.4



which is the more practical case because one would use all                               Fourth, the present design of VulDeePecker only accommo-
data available in practice.                                                          dates data flow analysis (i.e., data dependency), but not control
                                                                                     flow analysis (i.e., control dependency), despite the fact that the
    Therefore, it is fair to say that VulDeePecker substantially                     notion of code gadgets can accommodate data dependency and
outperforms two state-of-the-art code similarity-based vulnera-                      control dependency. It is an important future work to improve
bility detection systems, simply because VulDeePecker incurs                         the leverage of data flow analysis and accommodate control
a FPR of 5.7% and a FNR of 7.0% over the entire dataset.                             flow analysis to enhance vulnerability detection capabilities.
Nevertheless, it is important to note that deep learning-based
vulnerability detection largely rely on the amount of data. This                         Fifth, the present design of VulDeePecker uses some
leads to:                                                                            heuristics in labeling the ground truth of code gadgets, trans-
                                                                                     forming code gadgets into their symbolic representations,
    Insight 4: VulDeePecker is more effective than code                              transforming variable-length vector representations of code
similarity-based vulnerability detection systems, which cannot                       gadgets into fixed-length vectors. While intuitive, further re-
detect vulnerabilities that are not caused by code clones and                        search needs to be conducted to characterize the impact of
thus often incur high false negative rate. Nevertheless, the                         these heuristics on the effectiveness of VulDeePecker.
effectiveness of VulDeePecker is sensitive to the amount of
data, which appears to be inherent to the nature of deep                                 Sixth, the present implementation of VulDeePecker is
learning.                                                                            limited to the BLSTM neural network. We plan to conduct
                                                                                     systematic experiments with other kinds of neural networks
Using VulDeePecker in practice. In order to further show                             that could be used for vulnerability detection.
the usefulness of VulDeePecker, we collected 20 versions
of 3 software products: Xen, Seamonkey, and Libav. These                                 Seventh, the present evaluation of VulDeePecker is limited
products are different from the target programs mentioned                            because the dataset only contains buffer error vulnerabili-
above. We use VulDeePecker and the other vulnerability                               ties and resource management error vulnerabilities. We will
detection systems to detect the vulnerabilities in those software                    conduct experiments on all available types of vulnerabilities.
products. As highlighted in Table VI, VulDeePecker detected                          Although we further tested VulDeePecker against 3 software
4 vulnerabilities that have not been published in the NVD.                           products (i.e., Xen, Seamonkey, and Libav) and found 4 vulner-
We manually checked and confirmed these vulnerabilities,                             abilities that were not reported in the NVD and were “silently”
and found that they have been published for other products                           patched by the vendors when releasing later versions of these
and have been “silently” patched by the product vendors                              products, these vulnerabilities were known rather than 0-day
in the subsequent versions. In contrast, these vulnerabilities                       ones. Extensive experiments need to be conducted against more
are missed by almost all of the other vulnerability detection                        software products to check whether VulDeePecker has the
systems mentioned above, except that Flawfinder detects the                          capability in detecting 0-day vulnerabilities. In principle, this is
vulnerability corresponding to CVE-2015-4517 while missing                           possible because VulDeePecker uses pattern-based approach.
the other three.
                                                                                                                VI.       R ELATED W ORK
                              V.    L IMITATIONS                                        We classify the related prior work into two categories:
                                                                                     vulnerability detection (in relation to the purpose of the present
    The present design, implementation, and evaluation of
                                                                                     paper), and program analysis (in the relation to the means for
VulDeePecker have several limitations, which suggest inter-
                                                                                     vulnerability detection).
esting open problems for future research. First, the present
design of VulDeePecker is limited to dealing with vulnerability
detection by assuming source code of programs is available.                          A. Prior work in vulnerability detection
The detection of vulnerabilities in executables is a different                       Pattern-based approach. This approach can be further di-
and more challenging problem.                                                        vided to three categories. In the first category, patterns are
    Second, the present design of VulDeePecker only deals                            generated manually by human experts (e.g., open source tools
with C/C++ programs. Future research needs to be conducted                           Flawfinder [6], RATS [11], and ITS4 [52], commercial tools
to adapt it to deal with other kinds of programming languages.                       Checkmarx [2], Fortify [7], and Coverity [3]). These tools
                                                                                     often have high false positive rate or false negative rate. In
    Third, the present design of VulDeePecker only deals with                        the second category, patterns are generated semi-automatically
vulnerabilities related to library/API function calls. We will                       from pre-classified vulnerabilities ( e.g., missing check vulner-
investigate how to detect the other kinds of vulnerabilities by                      abilities [62], taint-style vulnerabilities [61], and information
leveraging the other kinds of key points mentioned above.                            leakage vulnerabilities [15]) and a pattern is specific to a type

                                                                               12

## Strona 13

of vulnerabilities. In the third category, patterns are generated            Somewhat related work is the use of deep learning for soft-
semi-automatically from type-agnostic vulnerabilities (i.e., no          ware defect prediction [54], [63]. However, software defects
need to pre-classify them into different types). These methods           are different from software vulnerabilities (i.e., methods for
use machine learning techniques, which rely on human experts             detecting defects cannot be used for detecting vulnerabilities
for defining features to characterize vulnerabilities [19], [37],        in general) [34], and the file-level representation of programs
[38], [49], [59], [60]. Moreover, these methods cannot pin               in [54] is too coarse-grained to pin down the locations of
down the precise locations of vulnerabilities because programs           vulnerabilities. Moreover, the defect prediction method pre-
are represented in coarse-grained granularity (e.g., program             sented in [63] is geared towards code changes rather than target
[19], package [37], component [38], [46], file [35], [49], and           programs as a whole. Remotely related work is the use of
function [59], [60]).                                                    deep learning for purposes, like software language modeling
                                                                         [57], code cloning detection [56], API learning [20], binary
    VulDeePecker falls into the pattern-based approach to vul-
                                                                         function boundary recognition [48], and malicious URLs, file
nerability detection. In contrast to the studies reviewed above,
                                                                         paths detection and registry keys detection [45].
VulDeePecker has two advantages. First, it does not need
human experts to define features for distinguishing vulnerable
code and non-vulnerable code. Second, it uses a fine-grained                                  VII.    C ONCLUSION
granularity to represent programs, and therefore can pin down                We have presented VulDeePecker, the first deep learning-
the precise locations of vulnerabilities.                                based vulnerability detection system, which aims to relieve
Code similarity-based approach. This approach has three                  human experts from the tedious and subjective work of man-
steps. The first step is to divide a program into some code              ually defining features and reduce the false negatives that are
fragments [25], [28], [31], [41], [44]. The second step is to            incurred by other vulnerability detection systems. Since deep
represent each code fragment in the abstract fashion, including          learning is invented for applications that are very different from
tokens [25], [28], [44], trees [26], [41], and graphs [31], [41].        vulnerability detection, we have presented some preliminary
The third step is to compute the similarity between code                 principles for guiding the practice of applying deep learning
fragments via their abstract representations obtained in the             to vulnerability detection. These principles should be further
second step.                                                             refined because deep learning has great potential in solving
                                                                         the problem of vulnerability detection. We have collected, and
    Compared with any pattern-based approach to vulnerability            made publicly available, a useful dataset for evaluating the
detection (including VulDeePacker), the code similarity-based            effectiveness of VulDeePecker and other deep learning-based
approach has the advantage that a single instance of vulnerable          vulnerability detection systems that will be developed in the
code is sufficient for detecting the same vulnerability in target        future. Systematic experiments show that VulDeePecker can
programs. But it can only detect vulnerabilities in the Type             achieve much lower false negative rate than other vulnerability
I and Type II code clones [42] (i.e., identical or almost-               detection systems, while relieving human experts from the
identical code clones), and some Type III code clones [42]               tedious work of manually defining features. For the 3 software
(e.g., deletion, insertion, and rearrangement of statements).            products we experimented with (i.e., Xen, Seamonkey, and
In order to achieve a higher effectiveness of vulnerability              Libav), VulDeePecker detected 4 vulnerabilities, which were
detection, human experts need to define features in order                not reported in the NVD and were “silently” patched by the
to automatically select the right code similarity algorithms             vendors when they released later versions of these products.
for different kinds of vulnerabilities [32]. However, even the           In contrast, the other detection systems missed almost all of
enhanced approach with expert-defined features [32] cannot               these vulnerabilities, except that one system detected 1 of these
detect vulnerabilities that are not caused by code clones. In            vulnerabilities and missed the other three vulnerabilities.
contrast, VulDeePecker can detect vulnerabilities that may or
may not caused by code clones, in an automatic fashion (i.e.,               Open problems for future research are abundant, including
no need of human expert to define features).                             the limitations of the present study discussed in Section
                                                                         V. In particular, precisely characterizing the capabilities and
B. Prior work related to using deep learning for program                 limitations of deep learning-based vulnerability detection is an
analysis                                                                 exciting research problem.
    To the best of our knowledge, we are the first to use deep                                ACKNOWLEDGMENT
learning to detect software vulnerabilities, as inspired by the
success of deep learning in image processing, speech recogni-                We thank the anonymous reviewers for their comments
tion, and natural language processing [21], [30], [40]. In order         that helped us improve the paper, and Marcus Pendleton for
to use deep learning for detecting software vulnerabilities,             proofreading the paper. This paper is supported by the Na-
programs need to be represented in vectors. There are two                tional Basic Research Program of China (973 Program) under
approaches for this purpose. One is to map the tokens extracted          grant No.2014CB340600, the National Science Foundation of
from programs, such as data types, variable names, function              China under grant No. 61672249, the Shenzhen Fundamental
names, and keywords, to vectors [57]; the other is to map                Research Program under grant No. JCYJ20170413114215614,
the nodes of abstract syntax trees extracted from programs,              and the Natural Science Foundation of Hebei Province under
such as function definitions, function invocations, identifier           grant No. F2015201089. Shouhuai Xu is supported in part
declarations, and control flow nodes, to vectors [36], [54].             by NSF Grant #1111925 and ARO Grant #W911NF-17-1-
VulDeePecker maps the tokens extracted from code gadgets                 0566. Any opinions, findings, conclusions or recommendations
to vectors, while taking it into consideration that the lines of         expressed in this material are those of the authors and do not
code in the code gadget is not necessarily consecutive.                  reflect the views of the funding agencies.

                                                                    13

## Strona 14

R EFERENCES                                              [30]   A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classification
                                                                                               with deep convolutional neural networks,” in Advances in Neural
 [1] C/C++ standard library functions, http://en.cppreference.com/w.                           Information Processing Systems, 2012, pp. 1097–1105.
 [2] Checkmarx, https://www.checkmarx.com/.                                             [31]   J. Li and M. D. Ernst, “CBCD: Cloned buggy code detector,” in Pro-
                                                                                               ceedings of the 34th International Conference on Software Engineering.
 [3] Coverity, https://scan.coverity.com/.
                                                                                               IEEE, 2012, pp. 310–320.
 [4] CVE, http://cve.mitre.org/.
                                                                                        [32]   Z. Li, D. Zou, S. Xu, H. Jin, H. Qi, and J. Hu, “VulPecker: An
 [5] Cyber Grand Challenge, https://www.cybergrandchallenge.com/.                              automated vulnerability detection system based on code similarity
 [6] FlawFinder, http://www.dwheeler.com/flawfinder.                                           analysis,” in Proceedings of the 32nd Annual Conference on Computer
                                                                                               Security Applications. ACM, 2016, pp. 201–213.
 [7] HP Fortify, https://www.hpfod.com/.
                                                                                        [33]   S. Montemagni and V. Pirelli, “Augmenting WordNet-like lexical re-
 [8] Keras, https://github.com/fchollet/keras.                                                 sources with distributional evidence. an application-oriented perspec-
 [9] Linux kernel API functions, https://www.kernel.org/doc/htmldocs/                          tive,” in Proceedings of the COLING/ACL Workshop on Use of WordNet
     kernel-api/.                                                                              in Natural Language Processing Systems, 1998, pp. 87–93.
[10] NVD, https://nvd.nist.gov/.                                                        [34]   P. Morrison, K. Herzig, B. Murphy, and L. Williams, “Challenges with
[11] Rough Audit Tool for Security, https://code.google.com/archive/p/                         applying vulnerability prediction models,” in Proceedings of the 2015
     rough-auditing-tool-for-security/.                                                        Symposium and Bootcamp on the Science of Security. ACM, 2015,
                                                                                               pp. 1–9.
[12] Software Assurance Reference Dataset, https://samate.nist.gov/SRD/
                                                                                        [35]   S. Moshtari and A. Sami, “Evaluating and comparing complexity,
     index.php.
                                                                                               coupling and a new proposed set of coupling metrics in cross-project
[13] Windows API functions, https://msdn.microsoft.com/en-us/library/                          vulnerability prediction,” in Proceedings of the 31st Annual ACM
     windows/desktop/ff818516(v=vs.85).aspx#user interface.                                    Symposium on Applied Computing. ACM, 2016, pp. 1415–1421.
[14]   word2vec, http://radimrehurek.com/gensim/models/word2vec.html.                   [36]   L. Mou, G. Li, Y. Liu, H. Peng, Z. Jin, Y. Xu, and L. Zhang,
[15]   M. Backes, B. Köpf, and A. Rybalchenko, “Automatic discovery and                       “Building program vector representations for deep learning,” arXiv
       quantification of information leaks,” in Proceedings of the 30th IEEE                   preprint arXiv:1409.3358, 2014.
       Symposium on Security and Privacy. IEEE, 2009, pp. 141–153.                      [37]   S. Neuhaus and T. Zimmermann, “The beauty and the beast: Vulner-
[16]   Y. Bengio, “Learning deep architectures for AI,” Foundations and                        abilities in Red Hat’s packages.” in Proceedings of the 2009 USENIX
       Trends in Machine Learning, vol. 2, no. 1, pp. 1–127, 2009.                             Annual Technical Conference. USENIX, 2009, pp. 527–538.
[17]   K. Cho, B. Van Merriënboer, D. Bahdanau, and Y. Bengio, “On the                 [38]   S. Neuhaus, T. Zimmermann, C. Holler, and A. Zeller, “Predicting
       properties of neural machine translation: Encoder-decoder approaches,”                  vulnerable software components,” in Proceedings of the 14th ACM
       arXiv preprint arXiv:1409.1259, 2014.                                                   conference on Computer and communications security. ACM, 2007,
                                                                                               pp. 529–540.
[18]   L. V. Davi, “Code-reuse attacks and defenses,” Ph.D. dissertation,
       Darmstadt University of Technology, Germany, 2015.                               [39]   M. Pendleton, R. Garcia-Lebron, J. Cho, and S. Xu, “A survey on
                                                                                               systems security metrics,” ACM Comput. Surv., vol. 49, no. 4, pp. 62:1–
[19]   G. Grieco, G. L. Grinblat, L. Uzal, S. Rawat, J. Feist, and L. Mounier,                 62:35, 2017.
       “Toward large-scale vulnerability discovery using machine learning,”
       in Proceedings of the 6th ACM Conference on Data and Application                 [40]   J. Pennington, R. Socher, and C. D. Manning, “Glove: Global vectors
       Security and Privacy. ACM, 2016, pp. 85–96.                                             for word representation.” in Proceedings of the 2014 Conference on
                                                                                               Empirical Methods in Natural Language Processing, vol. 14, 2014, pp.
[20]   X. Gu, H. Zhang, D. Zhang, and S. Kim, “Deep API learning,” in                          1532–1543.
       Proceedings of the 24th ACM SIGSOFT International Symposium on
       Foundations of Software Engineering. ACM, 2016, pp. 631–642.                     [41]   N. H. Pham, T. T. Nguyen, H. A. Nguyen, and T. N. Nguyen, “Detection
                                                                                               of recurring software vulnerabilities,” in Proceedings of the IEEE/ACM
[21]   G. Hinton, L. Deng, D. Yu, G. E. Dahl, A.-r. Mohamed, N. Jaitly,                        International Conference on Automated Software Engineering. ACM,
       A. Senior, V. Vanhoucke, P. Nguyen, T. N. Sainath, and B. Kingsbury,                    2010, pp. 447–456.
       “Deep neural networks for acoustic modeling in speech recognition:
       The shared views of four research groups,” IEEE Signal Processing                [42]   D. Rattan, R. Bhatia, and M. Singh, “Software clone detection: A
       Magazine, vol. 29, no. 6, pp. 82–97, 2012.                                              systematic review,” Information and Software Technology, vol. 55, no. 7,
                                                                                               pp. 1165–1199, 2013.
[22]   S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural
                                                                                        [43]   D. Rumelhart, J. McClelland, and G. Hinton, “Distributed representa-
       Computation, vol. 9, no. 8, pp. 1735–1780, 1997.
                                                                                               tions,” Parallel Distributed Processing: Explorations in the Microstruc-
[23]   S. Horwitz, T. Reps, and D. Binkley, “Interprocedural slicing using                     ture of Cognition, vol. 1, pp. 77–109, 1986.
       dependence graphs,” ACM Transactions on Programming Languages
                                                                                        [44]   H. Sajnani, V. Saini, J. Svajlenko, C. K. Roy, and C. V. Lopes, “Sourcer-
       and Systems (TOPLAS), vol. 12, no. 1, pp. 26–60, 1990.
                                                                                               erCC: Scaling code clone detection to big-code,” in Proceedings of the
[24]   B. James, B. Olivier, B. Frédéric, L. Pascal, and P. Razvan, “Theano: A               38th International Conference on Software Engineering. ACM, 2016,
       CPU and GPU math expression compiler,” in Proceedings of the Python                     pp. 1157–1168.
       for Scientific Computing Conference (SciPy), 2010.
                                                                                        [45]   J. Saxe and K. Berlin, “eXpose: A character-level convolutional neural
[25]   J. Jang, A. Agrawal, and D. Brumley, “ReDeBug: Finding unpatched                        network with embeddings for detecting malicious URLs, file paths and
       code clones in entire OS distributions,” in Proceedings of the 33th IEEE                registry keys,” arXiv preprint arXiv:1702.08568, 2017.
       Symposium on Security and Privacy. IEEE, 2012, pp. 48–62.
                                                                                        [46]   R. Scandariato, J. Walden, A. Hovsepyan, and W. Joosen, “Predicting
[26]   L. Jiang, G. Misherghi, Z. Su, and S. Glondu, “Deckard: Scalable and                    vulnerable software components via text mining,” IEEE Transactions
       accurate tree-based detection of code clones,” in Proceedings of the 29th               on Software Engineering, vol. 40, no. 10, pp. 993–1006, 2014.
       International Conference on Software Engineering. IEEE Computer                  [47]   M. Schuster and K. K. Paliwal, “Bidirectional recurrent neural net-
       Society, 2007, pp. 96–105.                                                              works,” IEEE Transactions on Signal Processing, vol. 45, no. 11, pp.
[27]   R. Jozefowicz, W. Zaremba, and I. Sutskever, “An empirical exploration                  2673–2681, 1997.
       of recurrent network architectures,” in Proceedings of the 32nd Inter-           [48]   E. C. R. Shin, D. Song, and R. Moazzezi, “Recognizing functions in
       national Conference on Machine Learning, 2015, pp. 2342–2350.                           binaries with neural networks.” in Proceedings of the 24th USENIX
[28]   S. Kim, S. Woo, H. Lee, and H. Oh, “VUDDY: A scalable approach                          Security Symposium. USENIX Associatioin, 2015, pp. 611–626.
       for vulnerable code clone discovery,” in Proceedings of the 38th IEEE            [49]   Y. Shin, A. Meneely, L. Williams, and J. A. Osborne, “Evaluating
       Symposium on Security and Privacy, 2017.                                                complexity, code churn, and developer activity metrics as indicators of
[29]   D. Kingma and J. Ba, “Adam: A method for stochastic optimization,”                      software vulnerabilities,” IEEE Transactions on Software Engineering,
       arXiv preprint arXiv:1412.6980, 2014.                                                   vol. 37, no. 6, pp. 772–787, 2011.


                                                                                   14

## Strona 15

[50]   S. Sinha, M. J. Harrold, and G. Rothermel, “System-dependence-                    layer l at the time t is:
       graph-based slicing of programs with arbitrary interprocedural control
       flow,” in Proceedings of the 1999 International Conference on Software                                        hlt = olt        tanh(clt ),
       Engineering. IEEE, 1999, pp. 432–441.
[51]   J. Su, Z. Tan, D. Xiong, and Y. Liu, “Lattice-based recurrent neural              where the output gate olt of the layer l at the time t is:
       network encoders for neural machine translation,” in Proceedings of the
       31st AAAI Conference on Artificial Intelligence, 2017, pp. 3302–3308.                        olt = σ(Wxo
                                                                                                             l
                                                                                                                xlt + Who
                                                                                                                       l
                                                                                                                          hlt−1 + Wco
                                                                                                                                   l l
                                                                                                                                      ct + blo )
[52]   J. Viega, J. T. Bloch, Y. Kohno, and G. McGraw, “ITS4: A static
       vulnerability scanner for C and C++ code,” in Proceedings of the 16th
                                                                                         and the state of LSTM cell clt of the layer l at the time t is:
       Annual Computer Security Applications Conference. IEEE, 2000, pp.
       257–267.
                                                                                           clt = ftl     clt−1 + ilt              l
                                                                                                                            tanh(Wxc xlt + Whc
                                                                                                                                            l
                                                                                                                                               hlt−1 + blc ).
[53]   O. Vinyals, A. Toshev, S. Bengio, and D. Erhan, “Show and tell: A
       neural image caption generator,” in Proceedings of the IEEE Conference                The forget gate ftl and the input gate ilt of the layer l at
       on Computer Vision and Pattern Recognition, 2015, pp. 3156–3164.                  the time t are calculated as follows:
[54]   S. Wang, T. Liu, and L. Tan, “Automatically learning semantic fea-
       tures for defect prediction,” in Proceedings of the 38th International                ftl         l
                                                                                                    = σ(Wxf xlt + Whf
                                                                                                                   l
                                                                                                                      hlt−1 + Wcf
                                                                                                                               l
                                                                                                                                  clt−1 + blf ),
       Conference on Software Engineering. ACM, 2016, pp. 297–308.
                                                                                              ilt        l
                                                                                                    = σ(Wxi xlt + Whi
                                                                                                                   l
                                                                                                                      hlt−1 + Wci
                                                                                                                               l l
                                                                                                                                  ct−1 + bli ),
[55]   M. Weiser, “Program slicing,” IEEE Transactioins on Software Engi-
       neering, vol. 10, no. 4, 1984.                                                    where xlt is the input to layer l − 1 (l > 1) or the input of
[56]   M. White, M. Tufano, C. Vendome, and D. Poshyvanyk, “Deep learning                                                l     l      l      l
                                                                                         the network (l = 1), Wxi          , Wxf , Wxo  , Wxc   are the weight
       code fragments for code clone detection,” in Proceedings of the 31st                                           l
       IEEE/ACM International Conference on Automated Software Engineer-                 matrices connecting xt with the input gate, the forget gate, the
                                                                                                                                         l     l      l      l
       ing. ACM, 2016, pp. 87–98.                                                        output gate, and the LSTM cell input, Whi         , Whf  , Who , Whc
                                                                                                                                      l
[57]   M. White, C. Vendome, M. Linares-Vásquez, and D. Poshyvanyk,                     are the weight matrices connecting ht−1 with the input gate,
       “Toward deep learning software repositories,” in Proceedings of the               the forget gate, the output gate, and the LSTM cell input, and
       12th Working Conference on Mining Software Repositories. IEEE,                    bli , blf , blo , blc are the bias items of the input gate, the forget
       2015, pp. 334–345.
                                                                                         gate, the output gate, and the LSTM cell input.
[58]   L. Wolf, Y. Hanani, K. Bar, and N. Dershowitz, “Joint word2vec
       networks for bilingual semantic representations,” International Journal
       of Computational Linguistics and Applications, vol. 5, no. 1, pp. 27–44,          B. Library/API function calls selected by Checkmarx
       2014.
[59]   F. Yamaguchi, F. Lindner, and K. Rieck, “Vulnerability extrapolation:                 Table VII summarizes the C/C++ library/API function calls
       Assisted discovery of vulnerabilities using machine learning,” in Pro-            related to the two types of vulnerabilities, buffer error (CWE-
       ceedings of the 5th USENIX Conference on Offensive Technologies.                  119) and resource management error (CWE-399), where “*”
       USENIX Association, 2011, pp. 13–13.                                              represents the wildcard. These library/API function calls are
[60]   F. Yamaguchi, M. Lottmann, and K. Rieck, “Generalized vulnerability               generated by the commercial product Checkmarx [2].
       extrapolation using abstract syntax trees,” in Proceedings of the 28th
       Annual Computer Security Applications Conference. ACM, 2012, pp.                   Table VII.     L IBRARY /API FUNCTION CALLS RELATED TO TWO TYPES
       359–368.                                                                                                        OF VULNERABILITIES
[61]   F. Yamaguchi, A. Maier, H. Gascon, and K. Rieck, “Automatic inference
                                                                                          CWE ID       C/C++ library/API function calls related to vulnerabilities
       of search patterns for taint-style vulnerabilities,” in Proceedings of the
       2015 IEEE Symposium on Security and Privacy. IEEE, 2015, pp.                       CWE-119      cin, getenv, getenv s, wgetenv, wgetenv s, catgets, gets, getchar,
                                                                                                       getc, getch, getche, kbhit, stdin, getdlgtext, getpass, scanf,
       797–812.
                                                                                                       fscanf, vscanf, vfscanf, istream.get, istream.getline, istream.peek,
[62]   F. Yamaguchi, C. Wressnegger, H. Gascon, and K. Rieck, “Chucky:                                 istream.read*, istream.putback, streambuf.sbumpc, streambuf.sgetc,
       Exposing missing checks in source code for vulnerability discovery,”                            streambuf.sgetn,          streambuf.snextc,           streambuf.sputbackc,
       in Proceedings of the 2013 ACM SIGSAC Conference on Computer &                                  SendMessage,          SendMessageCallback,            SendNotifyMessage,
       Communications Security. ACM, 2013, pp. 499–510.                                                PostMessage, PostThreadMessage, recv, recvfrom, Receive,
                                                                                                       ReceiveFrom, ReceiveFromEx, Socket.Receive*, memcpy, wmemcpy,
[63]   X. Yang, D. Lo, X. Xia, Y. Zhang, and J. Sun, “Deep learning for just-in-                         memccpy, memmove, wmemmove, memset, wmemset, memcmp,
       time defect prediction,” in Proceedings of the 2015 IEEE International                          wmemcmp, memchr, wmemchr, strncpy,                     strncpy*, lstrcpyn,
       Conference on Software Quality, Reliability and Security. IEEE, 2015,                             tcsncpy*, mbsnbcpy*, wcsncpy*, wcsncpy, strncat, strncat*,
       pp. 17–26.                                                                                        mbsncat*, wcsncat*, bcopy, strcpy, lstrcpy, wcscpy, tcscpy,
                                                                                                         mbscpy, CopyMemory, strcat, lstrcat, lstrlen, strchr, strcmp,
                                                                                                       strcoll, strcspn, strerror, strlen, strpbrk, strrchr, strspn, strstr, strtok,
                                                                                                       strxfrm, readlink, fgets, sscanf, swscanf, sscanf s, swscanf s, printf,
                                 A PPENDIX                                                             vprintf, swprintf, vsprintf, asprintf, vasprintf, fprintf, sprint, snprintf,
                                                                                                         snprintf*, snwprintf*, vsnprintf, CString.Format, CString.FormatV,
A. LSTM cells                                                                                          CString.FormatMessage,           CStringT.Format,        CStringT.FormatV,
                                                                                                       CStringT.FormatMessage, CStringT.FormatMessageV, syslog, malloc,
    The BLSTM layers in the BLSTM neural network contain                                               Winmain, GetRawInput*, GetComboBoxInfo, GetWindowText,
                                                                                                       GetKeyNameText, Dde*, GetFileMUI*, GetLocaleInfo*, GetString*,
a complex structure called LSTM cells, which are briefly                                               GetCursor*, GetScroll*, GetDlgItem*, GetMenuItem*
reviewed below and referred to [22] for greater details.                                  CWE-399      free, delete, new, malloc, realloc, calloc, alloca, strdup, asprintf,
                                                                                                       vsprintf, vasprintf, sprintf, snprintf, snprintf, snwprintf, vsnprintf
    Let denote the element-wise multiplication, tanh denote
the hyperbolic tangent function exp(x)−exp(−x)
                                 exp(x)+exp(−x) , and σ denote
                          1
the sigmoid function 1+exp(−x) .
    Each LSTM cell, denoted by c, uses an input gate i (i.e.,
the input data), a forget gate f (i.e., the state flow of the cell),
and an output gate o (i.e., the output of module) to control
the data flow through the neural network. The output hlt of the

                                                                                    15

## Strona 16

