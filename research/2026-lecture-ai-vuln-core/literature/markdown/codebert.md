# codebert

Źródło: `codebert.pdf`

## Strona 1

CodeBERT:
                                                      A Pre-Trained Model for Programming and Natural Languages
                                                       Zhangyin Feng1∗, Daya Guo2∗, Duyu Tang3 , Nan Duan3 , Xiaocheng Feng1
                                                    Ming Gong4 , Linjun Shou4 , Bing Qin1 , Ting Liu1 , Daxin Jiang4 , Ming Zhou3
                                         1
                                           Research Center for Social Computing and Information Retrieval, Harbin Institute of Technology, China
                                                       2
                                                         The School of Data and Computer Science, Sun Yat-sen University, China
                                                                        3
                                                                          Microsoft Research Asia, Beijing, China
                                                                4
                                                                  Microsoft Search Technology Center Asia, Beijing, China
                                                                  {zyfeng,xcfeng,qinb,tliu}@ir.hit.edu.cn
                                                                            guody5@mail2.sysu.edu.cn
                                                  {dutang,nanduan,migon,lisho,djiang,mingzhou}@microsoft.com




arXiv:2002.08155v4 [cs.CL] 18 Sep 2020
                                                                      Abstract                                and RoBERTa (Liu et al., 2019) have dramati-
                                                                                                              cally improved the state-of-the-art on a variety of
                                                  We present CodeBERT, a bimodal pre-trained                  natural language processing (NLP) tasks. These
                                                  model for programming language (PL) and                     pre-trained models learn effective contextual repre-
                                                  natural language (NL). CodeBERT learns                      sentations from massive unlabeled text optimized
                                                  general-purpose representations that support
                                                                                                              by self-supervised objectives, such as masked
                                                  downstream NL-PL applications such as nat-
                                                  ural language code search, code documen-                    language modeling, which predicts the original
                                                  tation generation, etc. We develop Code-                    masked word from an artificially masked input
                                                  BERT with Transformer-based neural architec-                sequence. The success of pre-trained models in
                                                  ture, and train it with a hybrid objective func-            NLP also drives a surge of multi-modal pre-trained
                                                  tion that incorporates the pre-training task of             models, such as ViLBERT (Lu et al., 2019) for
                                                  replaced token detection, which is to detect                language-image and VideoBERT (Sun et al., 2019)
                                                  plausible alternatives sampled from generators.
                                                                                                              for language-video, which are learned from bi-
                                                  This enables us to utilize both “bimodal” data
                                                  of NL-PL pairs and “unimodal” data, where
                                                                                                              modal data such as language-image pairs with bi-
                                                  the former provides input tokens for model                  modal self-supervised objectives.
                                                  training while the latter helps to learn bet-                  In this work, we present CodeBERT, a bimodal
                                                  ter generators. We evaluate CodeBERT on                     pre-trained model for natural language (NL) and
                                                  two NL-PL applications by fine-tuning model                 programming language (PL) like Python, Java,
                                                  parameters. Results show that CodeBERT                      JavaScript, etc. CodeBERT captures the seman-
                                                  achieves state-of-the-art performance on both
                                                                                                              tic connection between natural language and pro-
                                                  natural language code search and code docu-
                                                  mentation generation. Furthermore, to inves-                gramming language, and produces general-purpose
                                                  tigate what type of knowledge is learned in                 representations that can broadly support NL-PL
                                                  CodeBERT, we construct a dataset for NL-PL                  understanding tasks (e.g. natural language code
                                                  probing, and evaluate in a zero-shot setting                search) and generation tasks (e.g. code documen-
                                                  where parameters of pre-trained models are                  tation generation). It is developed with the multi-
                                                  fixed. Results show that CodeBERT performs                  layer Transformer (Vaswani et al., 2017), which is
                                                  better than previous pre-trained models on NL-
                                                                                                              adopted in a majority of large pre-trained models.
                                                  PL probing.1
                                                                                                              In order to make use of both bimodal instances
                                                                                                              of NL-PL pairs and large amount of available uni-
                                              1   Introduction
                                                                                                              modal codes, we train CodeBERT with a hybrid
                                              Large pre-trained models such as ELMo (Peters                   objective function, including standard masked lan-
                                              et al., 2018), GPT (Radford et al., 2018), BERT                 guage modeling (Devlin et al., 2018) and replaced
                                              (Devlin et al., 2018), XLNet (Yang et al., 2019)                token detection (Clark et al., 2020), where uni-
                                                                                                              modal codes help to learn better generators for
                                                   ∗
                                                     Work done while this author was an intern at Microsoft   producing better alternative tokens for the latter
                                              Research Asia.
                                                 1
                                                     All the codes and data are available at https://
                                                                                                              objective.
                                              github.com/microsoft/CodeBERT                                      We train CodeBERT from Github code reposito-

## Strona 2

ries in 6 programming languages, where bimodal          annotation. Dominant learning objectives are lan-
datapoints are codes that pair with function-level      guage modeling and its variations. For example,
natural language documentations (Husain et al.,         in GPT (Radford et al., 2018), the learning objec-
2019). Training is conducted in a setting similar       tive is language modeling, namely predicting the
to that of multilingual BERT (Pires et al., 2019),      next word wk given the preceding context words
in which case one pre-trained model is learned for      {w1 , w2 , ..., wk−1 }. As the ultimate goal of pre-
6 programming languages with no explicit mark-          training is not to train a good language model, it is
ers used to denote the input programming lan-           desirable to consider both preceding and following
guage. We evaluate CodeBERT on two down-                contexts to learn better general-purpose contextual
stream NL-PL tasks, including natural language          representations. This leads us to the masked lan-
code search and code documentation generation.          guage modeling objective used in BERT (Devlin
Results show that fine-tuning the parameters of         et al., 2018), which learns to predict the masked
CodeBERT achieves state-of-the-art performance          words of a randomly masked word sequence given
on both tasks. To further investigate what type of      surrounding contexts. Masked language modeling
knowledge is learned in CodeBERT, we construct          is also used as one of the two learning objectives
a dataset for NL-PL probing, and test CodeBERT          for training CodeBERT.
in a zero-shot scenario, i.e. without fine-tuning the
parameters of CodeBERT. We find that CodeBERT           2.2   Multi-Modal Pre-Trained Models
consistently outperforms RoBERTa, a purely natu-
ral language-based pre-trained model. The contri-       The remarkable success of the pre-trained model
butions of this work are as follows:                    in NLP has driven the development of multi-modal
                                                        pre-trained model that learns implicit alignment
    • CodeBERT is the first large NL-PL pre-            between inputs of different modalities. These mod-
      trained model for multiple programming lan-       els are typically learned from bimodal data, such
      guages.                                           as pairs of language-image or pairs of language-
                                                        video. For example, ViLBERT (Lu et al., 2019)
    • Empirical results show that CodeBERT is ef-       learns from image caption data, where the model
      fective in both code search and code-to-text      learns by reconstructing categories of masked im-
      generation tasks.                                 age region or masked words given the observed
                                                        inputs, and meanwhile predicting whether the cap-
    • We further created a dataset which is the first
                                                        tion describes the image content or not. Simi-
      one to investigate the probing ability of the
                                                        larly, VideoBERT (Sun et al., 2019) learns from
      code-based pre-trained models.
                                                        language-video data and is trained by video and
2     Background                                        text masked token prediction. Our work belongs
                                                        to this line of research as we regard NL and PL
2.1    Pre-Trained Models in NLP                        as different modalities. Our method differs from
Large pre-trained models (Peters et al., 2018; Rad-     previous works in that the fuels for model train-
ford et al., 2018; Devlin et al., 2018; Yang et al.,    ing include not only bimodal data of NL-PL pairs,
2019; Liu et al., 2019; Raffel et al., 2019) have       but larger amounts of unimodal data such as codes
brought dramatic empirical improvements on al-          without paired documentations.
most every NLP task in the past few years. Suc-            A concurrent work (Kanade et al., 2019) uses
cessful approaches train deep neural networks on        masked language modeling and next sentence pre-
large-scale plain texts with self-supervised learning   diction as the objective to train a BERT model on
objectives. One of the most representative neural       Python source codes, where a sentence is a log-
architectures is the Transformer (Vaswani et al.,       ical code line as defined by the Python standard.
2017), which is also the one used in this work. It      In terms of the pre-training process, CodeBERT
contains multiple self-attention layers, and can be     differs from their work in that (1) CodeBERT is
conventionally learned with gradient decent in an       trained in a cross-modal style and leverages both
end-to-end manner as every component is differen-       bimodal NL-PL data and unimodal PL/NL data, (2)
tiable. The terminology “self-supervised” means         CodeBERT is pre-trained over six programming
that supervisions used for pre-training are auto-       languages, and (3) CodeBERT is trained with a
matically collected from raw data without manual        new learning objective based on replaced token

## Strona 3

detection.                                                 T RAINING DATA      bimodal DATA     unimodal C ODES
                                                           GO                     319,256           726,768
3     CodeBERT                                             JAVA                   500,754          1,569,889
                                                           JAVA S CRIPT           143,252          1,857,835
We describe the details about CodeBERT in this             PHP                    662,907           977,821
                                                           P YTHON                458,219          1,156,085
section, including the model architecture, the input       RUBY                    52,905           164,048
and output representations, the objectives and data        A LL                  2,137,293         6,452,446
used for training CodeBERT, and how to fine-tune
CodeBERT when it is applied to downstream tasks.         Table 1: Statistics of the dataset used for training Code-
                                                         BERT.
3.1   Model Architecture
We follow BERT (Devlin et al., 2018) and                 provided by Husain et al. (2019), which includes
RoBERTa (Liu et al., 2019), and use multi-layer          2.1M bimodal datapoints and 6.4M unimodal codes
bidirectional Transformer (Vaswani et al., 2017) as      across six programming languages (Python, Java,
the model architecture of CodeBERT. We will not          JavaScript, PHP, Ruby, and Go). Data statistics is
review the ubiquitous Transformer architecture in        shown in Table 1.2
detail. We develop CodeBERT by using exactly the            The data comes from publicly available open-
same model architecture as RoBERTa-base. The             source non-fork GitHub repositories and are fil-
total number of model parameters is 125M.                tered with a set of constraints and rules. For ex-
                                                         ample, (1) each project should be used by at least
3.2   Input/Output Representations                       one other project, (2) each documentation is trun-
In the pre-training phase, we set the input as the       cated to the first paragraph, (3) documentations
concatenation of two segments with a special sepa-       shorter than three tokens are removed, (4) func-
rator token, namely [CLS], w1 , w2 , ..wn , [SEP ],      tions shorter than three lines are removed, and (5)
c1 , c2 , ..., cm , [EOS]. One segment is natural lan-   function names with substring “test” are removed.
guage text, and another is code from a certain pro-      An example of the data is given in Figure 1 3 .
gramming language. [CLS] is a special token in
front of the two segments, whose final hidden repre-
sentation is considered as the aggregated sequence
representation for classification or ranking. Follow-
ing the standard way of processing text in Trans-
former, we regard a natural language text as a se-
quence of words, and split it as WordPiece (Wu
et al., 2016). We regard a piece of code as a se-
quence of tokens.
   The output of CodeBERT includes (1) contextual
vector representation of each token, for both natural    Figure 1: An example of the NL-PL pair, where NL is
language and code, and (2) the representation of         the first paragraph (filled in red) from the documenta-
                                                         tion (dashed line in black) of a function.
[CLS], which works as the aggregated sequence
representation.
                                                         3.4   Pre-Training CodeBERT
3.3   Pre-Training Data
                                                         We describe the two objectives used for training
We train CodeBERT with both bimodal data, which
                                                         CodeBERT here. The first objective is masked
refers to parallel data of natural language-code
                                                         language modeling (MLM), which has proven ef-
pairs, and unimodal data, which stands for codes
                                                         fective in literature (Devlin et al., 2018; Liu et al.,
without paired natural language texts and natural
                                                             2
language without paired codes.                                 Since we will evaluate on the natural language code
                                                         search task, we only use the training data of Husain et al.
   We use datapoints from Github repositories,           (2019) to train CodeBERT with no access to the dev and test-
where each bimodal datapoint is an individual            ing data.
                                                             3
function with paired documentation, and each uni-              The source of the illustrating example comes from
                                                         https://github.com/apache/spark/blob/
modal code is a function without paired documen-         618d6bff71073c8c93501ab7392c3cc579730f0b/
tation. Specifically, we use a recent large dataset      python/pyspark/rdd.py#L125-L138

### Obrazy na stronie

- `image` obiekt 0: ![image strona 3 obiekt 0](pdfimages/codebert/codebert-000.png)

## Strona 4

CodeBERT V2:
A Pre-trained Model for NL-Code Understanding and Generation

                                                    sample
       𝑤1         [𝑀𝐴𝑆𝐾]𝑤                                      𝑤51                                                     replaced
       𝑤2           𝑤2                                          𝑤2                                                     original
       𝑤3           𝑤3            NL Generator                  𝑤3                                                     original
       𝑤4           𝑤4                                          𝑤4                                                     original
                                                    sample
       𝑤5         [𝑀𝐴𝑆𝐾]𝑤                                       𝑤5                                                     original


                                                                                         NL-Code
                                                                                       Discriminator
       𝑐1           𝑐1                                          𝑐1                                                     original
                                                    sample
       𝑐2         [𝑀𝐴𝑆𝐾]𝑐                                      𝑐29                                                     replaced
       𝑐3           𝑐3                                          𝑐3                                                     original
                                 Code Generator
       𝑐4           𝑐4                                          𝑐4                                                     original
       𝑐5           𝑐5                                          𝑐5                                                     original
                                                    sample
       𝑐6         [𝑀𝐴𝑆𝐾]𝑐                                      𝑐162                                                    replaced


Figure 2: An illustration about the replaced token detection objective. Both NL and code generators are language                         6
models, which generate plausible tokens for masked positions based on surrounding contexts. NL-Code discrimi-
nator is the targeted pre-trained model, which is trained via detecting plausible alternatives tokens sampled from
NL and PL generators. NL-Code discriminator is used for producing general-purpose representations in the fine-
tuning step. Both NL and code generators are thrown out in the fine-tuning step.


2019; Sun et al., 2019). We apply masked language            Objective #2: Replaced Token Detection (RTD)
modeling on bimodal data of NL-PL pairs. The sec-            In the MLM objective, only bimodal data (i.e. data-
ond objective is replaced token detection (RTD),             points of NL-PL pairs) is used for training. Here we
which further uses a large amount of unimodal data,          present the objective of replaced token detection.
such as codes without paired natural language texts.         The RTD objective (Clark et al., 2020) is origi-
Detailed hyper-parameters for model pre-training             nally developed for efficiently learning pre-trained
are given in Appendix B.1.                                   model for natural language. We adapt it in our sce-
                                                             nario, with the advantage of using both bimodal
Objective #1: Masked Language Modeling
                                                             and unimodal data for training. Specifically, there
(MLM) Given a datapoint of NL-PL pair (x =
                                                             are two data generators here, an NL generator pGw
{w, c}) as input, where w is a sequence of NL
                                                             and a PL generator pGc , both for generating plau-
words and c is a sequence of PL tokens, we first
                                                             sible alternatives for the set of randomly masked
select a random set of positions for both NL and PL
                                                             positions.
to mask out (i.e. mw and mc , respectively), and
then replace the selected positions with a special                    ŵi ∼ pGw (wi |wmasked ) for i ∈ mw                          (7)
[M ASK] token. Following Devlin et al. (2018),                                  Gc            masked               c
                                                                      cˆi ∼ p        (ci |c            ) for i ∈ m                 (8)
15% of the tokens from x are masked out.

         mw
          i ∼ unif{1, |w|} for i = 1 to |w|        (1)                wcorrupt = REPLACE(w, mw , ŵ)                               (9)
         mci ∼ unif{1, |c|} for i = 1 to |c|       (2)                 c   corrupt
                                                                                     = REPLACE(c, m , ĉ)      c
                                                                                                                                  (10)
       masked                     w                                        corrupt        corrupt        corrupt
  w             = REPLACE(w, m , [M ASK]) (3)                         x              =w             +c                            (11)
       masked                    c
   c            = REPLACE(c, m , [M ASK])          (4)
                                                             The discriminator is trained to determine whether
            x=w+c                                  (5)       a word is the original one or not, which is a binary
                                                             classification problem. It is worth noting that the
The MLM objective is to predict the original to-
                                                             RTD objective is applied to every position in the
kens which are masked out, formulated as follows,
                                                             input, and it differs from GAN (generative adver-
where pD1 is the discriminator which predicts a
                                                             sarial network) in that if a generator happens to
token from a large vocabulary.
                                                             produce the correct token, the label of that token
                                                             is “real” instead of “fake” (Clark et al., 2020). The
              X
LMLM (θ) =          −log pD1 (xi |wmasked ,cmasked )
                i∈mw ∪mc                                     loss function of RTD with regard to the discrimina-
                                                   (6)       tor parameterized by θ is given below, where δ(i) is

## Strona 5

an indicator function and pD2 is the discriminator            of CodeBERT are fixed. Finally, we evaluate Code-
that predicts the probability of the i-th word being          BERT on a generation problem, i.e. code documen-
original.                                                     tation generation (§4.3), and further evaluate on a
                                                              programming language which is never seen in the
             |w|+|c| 
                X                                             training phase (§4.4).
LRTD (θ) =               δ(i)log pD2 (xcorrupt , i)+
                i=1                                           4.1    Natural Language Code Search
                                              
                                  D2 corrupt
                1 − δ(i) 1 − log p (x        , i)             Given a natural language as the input, the objec-
                                                              tive of code search is to find the most semantically
                                                       (12)
                                                              related code from a collection of codes. We con-
                  (
                                 corrupt                      duct experiments on the CodeSearchNet corpus
                   1,        if xi    = xi .
           δ(i) =                                      (13)   (Husain et al., 2019) 4 . We follow the official evalu-
                   0,        otherwise.                       ation metric to calculate the Mean Reciprocal Rank
   There are many different ways to implement the             (MRR) for each pair of test data (c, w) over a fixed
generators. In this work, we implement two ef-                set of 999 distractor codes. We further calculate the
ficient n-gram language models (Jurafsky, 2000)               macro-average MRR for all languages as an overall
with bidirectional contexts, one for NL and one               evaluation metric. It is helpful to note that this met-
for PL, and learn them from corresponding uni-                ric differs from the AVG metric in the original pa-
model datapoints, respectively. The approach is               per, where the answer is retrieved from candidates
easily generalized to learn bimodal generators or             from all six languages. We fine-tune a language-
use more complicated generators like Transformer-             specific model for each programming language5 .
based neural architecture learned in a joint manner.          We train each model with a binary classification
We leave these to future work. The PL training data           loss function, where a sof tmax layer is connected
is the unimodal codes as shown in Table 1, and the            to the representation of [CLS]. Both training and
NL training data comes from the documentations                validation datasets are created in a way that posi-
from bimodal data. One could easily extend these              tive and negative samples are balanced. Negative
two training datasets to larger amount. The final             samples consist of balanced number of instances
loss function are given below.                                with randomly replaced NL (i.e. (c, ŵ)) and PL
                                                              (i.e. (ĉ, w)). Detailed hyper-parameters for model
             min LMLM (θ) + LRTD (θ)                   (14)   fine-tuning are given in Appendix B.2.
                 θ

3.5    Fine-Tuning CodeBERT                                   Model Comparisons Table 2 shows the results
                                                              of different approaches on the CodeSearchNet cor-
We have different settings to use CodeBERT in                 pus. The first four rows are reported by Husain
downstream NL-PL tasks. For example, in natural               et al. (2019), which are joint embeddings of NL and
language code search, we feed the input as the                PL (Gu et al., 2018; Mitra et al., 2018). NB OW
same way as the pre-training phase and use the                represents neural bag-of-words. CNN, B I RNN
representation of [CLS] to measure the semantic               and S ELFATT stand for 1D convolultional neu-
relevance between code and natural language query,            ral network (Kim, 2014), bidirectional GRU-based
while in code-to-text generation, we use an encoder-          recurrent neural network (Cho et al., 2014), and
decoder framework and initialize the encoder of               multi-head attention (Vaswani et al., 2017), respec-
a generative model with CodeBERT. Details are                 tively.
given in the experiment section.
                                                                 We report the remaining numbers in Table 2.
4     Experiment                                              We train all these pre-trained models by regarding
                                                              codes as a sequence of tokens. We also continu-
We present empirical results in this section to verify        ously train RoBERTa only on codes from Code-
the effectiveness of CodeBERT. We first describe              SearchNet with masked language modeling. Re-
the use of CodeBERT in natural language code                  sults show that CodeBERT consistently performs
search (§4.1), in a way that model parameters of
                                                                 4
CodeBERT are fine-tuned. After that, we present                    More details about the dataset are given in Appendix A.
                                                                 5
                                                                   We have fine-tuned a multi-lingual model for six program-
the NL-PL probing task (§4.2), and evaluate Code-             ming languages, but find that it performs worse that fine-tuning
BERT in a zero-shot setting where the parameters              a language-specific model for each programming language.

## Strona 6

MODEL                                      RUBY      JAVASCRIPT      GO      PYTHON     JAVA      PHP    M A -AVG
 NB OW                                     0.4285       0.4607      0.6409    0.5809    0.5140   0.4835    0.5181
 CNN                                       0.2450       0.3523      0.6274    0.5708    0.5270   0.5294    0.4753
 B I RNN                                   0.0835       0.1530      0.4524    0.3213    0.2865   0.2512    0.2580
 SELFATT                                   0.3651       0.4506      0.6809    0.6922    0.5866   0.6011    0.5628
 RO B ERTA                                 0.6245       0.6060      0.8204    0.8087    0.6659   0.6576    0.6972
 PT W / C ODE O NLY ( INIT = S )           0.5712       0.5557      0.7929    0.7855    0.6567   0.6172    0.6632
 PT W / C ODE O NLY ( INIT =R)             0.6612       0.6402      0.8191    0.8438    0.7213   0.6706    0.7260
 C ODE BERT (MLM, INIT = S )               0.5695       0.6029      0.8304    0.8261    0.7142   0.6556    0.6998
 C ODE BERT (MLM, INIT =R)                 0.6898       0.6997      0.8383    0.8647    0.7476   0.6893    0.7549
 C ODE BERT (RTD, INIT =R)                 0.6414       0.6512      0.8285    0.8263    0.7150   0.6774    0.7233
 C ODE BERT (MLM+RTD, INIT =R)             0.6926       0.7059      0.8400    0.8685    0.7484   0.7062    0.7603


Table 2: Results on natural language code retrieval. Baselines include four joint embeddings (first group) of NL
and PL, RoBERTa, and RoBERTa which is continuously trained with masked language modeling on codes only
(second group). PT stands for pre-training. We train CodeBERT (third group) with different settings, including
using different initialization (from scratch (INIT = S) or initialized with the parameters of RoBERTa (INIT =R)) and
using different learning objectives (MLM, RTD, or the combination of both).


better than RoBERTa and the model pre-trained                    is replaced by [M ASK] and distractor candidate
with code only. CodeBERT (MLM) learned from                      answers are curated based on our expertise.
scratch performs better than RoBERTa. Unsur-                        Specifically, we evaluate on the NL side and PL
prisingly, initializing CodeBERT with RoBERTa                    side, respectively. To ease the effort of data col-
improves the performance 6 .                                     lection, we collect data automatically from NL-PL
                                                                 pairs in both validation and testing sets of Code-
4.2   NL-PL Probing                                              SearchNet, both of which are unseen in the pre-
In the previous subsection, we show the empirical                training phase. To evaluate on the NL side, we
effectiveness of CodeBERT in a setting that the                  select NL-PL pairs whose NL documentations in-
parameters of CodeBERT are fine-tuned in down-                   clude one of the six keywords (max, maximize, min,
stream tasks. In this subsection, we further inves-              minimize, less, greater), and group them to four
tigate what type of knowledge is learned in Code-                candidates by merging first two keywords and the
BERT without modifying the parameters.                           middle two keywords. The task is to ask pre-trained
                                                                 models to select the correct one instead of three
Task Formulation and Data Construction Fol-                      other distractors. That is to say, the input in this
lowing the probing experiments in NLP (Petroni                   setting includes the complete code and a masked
et al., 2019; Talmor et al., 2019), we study NL-                 NL documentation. The goal is to select the correct
PL probing here. Since there is no existing work                 answer from four candidates. For the PL side, we
towards this goal, we formulate the problem of                   select codes containing keywords max and min, and
NL-PL probing and create the dataset by ourselves.               formulate the task as a two-choice answer selection
Given an NL-PL pair (c, w), the goal of NL-PL                    problem. Here, the input includes complete NL
probing is to test model’s ability to correctly pre-             documentation and a masked PL code, and the goal
dict/recover the masked token of interest (either a              is to select the correct answer from two candidates.
code token ci or word token wj ) among distractors.              Since code completion is an important scenario,
There are two major types of distractors: one is the             we would like to test model’s ability in predicting
whole target vocabulary used for the masked lan-                 the correct token merely based on preceding PL
guage modeling objective (Petroni et al., 2019), and             contexts. Therefore, we add an additional setting
another one has fewer candidates which are filter or             for PL side, where the input includes the complete
curated based on experts’ understanding about the                NL documentation and preceding PL codes. Data
ability to be tested (Talmor et al., 2019). We follow            statistics is given in the top two rows in Table 3.
the second direction and formulate NL-PL probing
as a multi-choice question answering task, where                 Model Comparisons Results are given in Table
the question is cloze-style in which a certain token             3. We report accuracy, namely the number of cor-
  6
    We further give a learning curve of different pre-trained    rectly predicted instances over the number of all
models in the fine-tuning process in Appendix C.                 instances, for each programming language. Since

## Strona 7

RUBY           JAVASCRIPT          GO        PYTHON           JAVA         PHP         ALL

   NUMBER OF DATAPOINTS FOR PROBING
   PL (2 CHOICES )                38                    272             152           1,264         482          407        2,615
   NL (4 CHOICES )                20                     65             159            216          323           73         856
   PL PROBING
   ROBERTA                      73.68                   63.97          72.37          59.18        59.96       69.78        62.45
   P RE -T RAIN W / C ODE O NLY 71.05                   77.94          89.47          70.41        70.12       82.31        74.11
   C ODE BERT (MLM)             86.84                   86.40          90.79          82.20        90.46       88.21        85.66
   PL PROBING WITH PRECEDING CONTEXT ONLY
   ROBERTA                      73.68                   53.31          51.32          55.14        42.32       52.58        52.24
   P RE -T RAIN W / C ODE O NLY 63.16                   48.53          61.84          56.25        58.51       58.97        56.71
   C ODE BERT (MLM)             65.79                   50.74          59.21          62.03        54.98       59.95        59.12
   NL PROBING
   ROBERTA                      50.00                   72.31          54.72          61.57        61.61       65.75        61.21
   P RE -T RAIN W / C ODE O NLY 55.00                   67.69          60.38          68.06        65.02       68.49        65.19
   C ODE BERT (MLM)             65.00                   89.23          66.67          76.85        73.37       79.45        74.53

Table 3: Statistics of the data for NL-PL probing and the performance of different pre-trained models. Accuracies
(%) are reported. Best results in each group are in bold.


datasets in different programming languages are                                                                masked NL token

extremely unbalanced, we report the accumulated            "Transforms a vector np.arange(-N, M, dx) to np.arange( min (|vec|),
                                                           max(N,M),dx)]"
metric with the same way. We use CodeBERT
                                                           def vec_to_halfvec(vec):
(MLM) here because its output layer naturally fits
for probing. Results show that CodeBERT per-                  d = vec[1:] - vec[:-1]
forms better than baselines on almost all languages           if ((d/d.mean()).std() > 1e-14) or (d.mean() < 0):
                                                                 raise ValueError('vec must be np.arange() in increasing order')
on both NL and PL probing. The numbers with                   dx = d.mean()                     masked PL token
only preceding contexts are lower than that with              lowest = np.abs(vec). min ()
bidirectional contexts, which suggests that code              highest = np.abs(vec).max()
                                                              return np.arange(lowest, highest + 0.1*dx, dx).astype(vec.dtype)
completion is challenging. We leave it as a future
work.                                                                                    max          min          less       greater
   We further give a case study on PL-NL probing.          NL
                                                                       Roberta          96.24%       3.73%        0.02%        0.01%

We mask NL token and PL token separately, and                     CodeBERT (MLM)        39.38%      60.60%        0.02%      0.0003%
                                                                       Roberta          95.85%       4.15%           -             -
report the predicted probabilities of RoBERTa and           PL
                                                                  CodeBERT (MLM)        0.001%     99.999%           -             -
CodeBERT. Figure 3 illustrates the example of a
python code7 . We can see that RoBERTa fails in           Figure 3: Case study on python language. Masked to-
both cases, whereas CodeBERT makes the correct            kens in NL (in blue) and PL (in yellow) are separately
prediction in both NL and PL settings.                    applied. Predicted probabilities of RoBERTa and Code-
                                                          BERT are given.
4.3   Code Documentation Generation
Although the pre-training objective of Code-              Model Comparisons We compare our model
BERT does not include generation-based objectives         with several baselines, including a RNN-based
(Lewis et al., 2019), we would like to investigate        model with attention mechanism (Sutskever et al.,
to what extent does CodeBERT perform on gen-              2014), the Transformer (Vaswani et al., 2017),
eration tasks. Specifically, we study code-to-NL          RoBERTa and the model pre-trained on code only.
generation, and report results for the documenta-         To demonstrate the effectiveness of CodeBERT
tion generation task on CodeSearchNet Corpus in           on code-to-NL generation tasks, we adopt various
six programming languages. Since the generated            pre-trained models as encoders and keep the hyper-
documentations are short and higher order n-grams         parameters consistent. Detailed hyper-parameters
may not overlap, we remedy this problem by using          are given in Appendix B.3.
smoothed BLEU score (Lin and Och, 2004).                     Table 4 shows the results with different mod-
                                                          els for the code-to-documentation generation task.
  7
    The  example  comes   from   https://                 As we can see, models pre-trained on program-
github.com/peri-source/peri/blob/
61beed5deaaf978ab31ed716e8470d86ba639867/                 ming language outperform RoBERTa, which illus-
peri/comp/psfcalc.py#L994-L1002                           trates that pre-trainning models on programming

## Strona 8

MODEL                        RUBY     JAVASCRIPT       GO      PYTHON    JAVA    PHP     OVERALL

           SEQ 2 SEQ                     9.64       10.21     13.98       15.93     15.09   21.08    14.32
           T RANSFORMER                 11.18       11.59     16.38       15.81     16.26   22.12    15.56
           RO BERTA                     11.17       11.90     17.72       18.14     16.47   24.02    16.57
           PRE - TRAIN W / CODE ONLY    11.91       13.99     17.78       18.58     17.50   24.34    17.35
           C ODE BERT ( RTD )           11.42       13.27     17.53       18.29     17.35   24.10    17.00
           C ODE BERT ( MLM )           11.57       14.41     17.78       18.77     17.38   24.85    17.46
           C ODE BERT ( RTD + MLM )     12.16       14.90     18.07       19.06     17.65   25.16    17.83

           Table 4: Results on Code-to-Documentation generation, evaluated with smoothed BLEU-4 score.


language could improve code-to-NL generation.                 could generalize better to other programming lan-
Besides, results in the Table 4 show that CodeBERT            guage which is never seen in the pre-training step.
pre-trained with RTD and MLM objectives brings                However, our model achieve slightly lower results
a gain of 1.3 BLEU score over RoBERTa overall                 than code2seq (Alon et al., 2019). The main reason
and achieve the state-of-the-art performance8 .               could be that code2seq makes use of compositional
                                                              paths in its abstract syntax tree (AST) while Code-
4.4      Generalization to Programming                        BERT only takes original code as the input. We
         Languages NOT in Pre-training                        have trained a version of CodeBERT by traversing
We would like to evaluate CodeBERT on the pro-                the tree structure of AST following a certain order,
gramming language which is never seen in the pre-             but applying that model does not bring improve-
training step. To this end, we study the task of gen-         ments on generation tasks. This shows a potential
erating a natural language summary of a C# code               direction to improve CodeBERT by incorporating
snippet. We conduct experiments on the dataset                AST.
of CodeNN (Iyer et al., 2016)9 , which consists of
66,015 pairs of questions and answers automati-               5        Conclusion
cally collected from StackOverflow. This dataset              In this paper, we present CodeBERT, which to the
is challenging since the scale of dataset is orders           best of our knowledge is the first large bimodal
of magnitude smaller than CodeSearchNet Corpus.               pre-trained model for natural language and pro-
We evaluate models using smoothed BLEU-4 score                gramming language. We train CodeBERT on both
and use the same evaluation scripts as Iyer et al.            bimodal and unimodal data, and show that fine-
(2016).                                                       tuning CodeBERT achieves state-of-the-art perfor-
                                                              mance on downstream tasks including natural lan-
  M ODEL                                         BLEU
                                                              guage code search and code-to-documentation gen-
  MOSES (KOEHN ET AL ., 2007)                     11.57
  IR                                              13.66
                                                              eration. To further investigate the knowledge em-
  SUM-NN (RUSH ET AL ., 2015)                     19.31       bodied in pre-trained models, we formulate the task
  2- LAYER B I LSTM                               19.78       of NL-PL probing and create a dataset for probing.
  T RANSFORMER (VASWANI ET AL ., 2017)            19.68
  T REE LSTM (TAI ET AL ., 2015)                  20.11       We regard the probing task as a cloze-style answer
  C ODE NN (I YER ET AL ., 2016)                  20.53       selection problem, and curate distractors for both
  CODE 2 SEQ (A LON ET AL ., 2019)                23.04       NL and PL parts. Results show that, with model
  RO BERTA                                        19.81
  PRE - TRAIN W / CODE ONLY                       20.65       parameters fixed, CodeBERT performs better than
  C ODE BERT (RTD)                                22.14       RoBERTa and a continuously trained model using
  C ODE BERT (MLM)                                22.32       codes only.
  C ODE BERT (MLM+RTD)                            22.36
                                                                 There are many potential directions for further
  Table 5: Code-to-NL generation on C# language.              research on this field. First, one could learn better
                                                              generators with bimodal evidence or more compli-
                                                              cated neural architecture to improve the replaced to-
Model Comparisons Table 5 shows that our                      ken detection objective. Second, the loss functions
model with MLM and RTD pre-training objectives                of CodeBERT mainly target on NL-PL understand-
achieves 22.36 BLEU score and improves by 2.55                ing tasks. Although CodeBERT achieves strong
points over RoBERTa, which illustrates CodeBERT               BLEU scores on code-to-documentation genera-
   8
       We further give some output examples in Appendix E.    tion, the CodeBERT itself could be further im-
   9
       https://github.com/sriniiyer/codenn                    proved by generation-related learning objectives.

## Strona 9

How to successfully incorporate AST into the pre-         Dan Jurafsky. 2000. Speech & language processing.
training step is also an attractive direction. Third,       Pearson Education India.
we plan to apply CodeBERT to more NL-PL re-               Aditya Kanade, Petros Maniatis, Gogul Balakrish-
lated tasks, and extend it to more programming              nan, and Kensen Shi. 2019. Pre-trained contex-
languages. Flexible and powerful domain/language            tual embedding of source code. arXiv preprint
adaptation methods are necessary to generalize              arXiv:2001.00059.
well.                                                     Yoon Kim. 2014.         Convolutional neural net-
                                                            works for sentence classification. arXiv preprint
Acknowledgments                                             arXiv:1408.5882.

Xiaocheng Feng is the corresponding author of this        Philipp Koehn, Hieu Hoang, Alexandra Birch, Chris
work. We thank the anonymous reviewers for their            Callison-Burch, Marcello Federico, Nicola Bertoldi,
insightful comments. Zhangyin Feng, Xiaocheng               Brooke Cowan, Wade Shen, Christine Moran,
                                                            Richard Zens, et al. 2007. Moses: Open source
Feng, Bing Qin and Ting Liu are supported by the            toolkit for statistical machine translation. In Pro-
National Key R&D Program of China via grant                 ceedings of the 45th annual meeting of the associ-
2018YFB1005103 and National Natural Science                 ation for computational linguistics companion vol-
Foundation of China (NSFC) via grant 61632011               ume proceedings of the demo and poster sessions,
                                                            pages 177–180.
and 61772156.
                                                          Mike Lewis, Yinhan Liu, Naman Goyal, Mar-
                                                            jan Ghazvininejad, Abdelrahman Mohamed, Omer
References                                                  Levy, Ves Stoyanov, and Luke Zettlemoyer. 2019.
                                                            Bart: Denoising sequence-to-sequence pre-training
Uri Alon, Shaked Brody, Omer Levy, and Eran Yahav.          for natural language generation, translation, and
  2019. code2seq: Generating sequences from struc-          comprehension. arXiv preprint arXiv:1910.13461.
  tured representations of code. International Confer-
  enceon Learning Representations.                        Chin-Yew Lin and Franz Josef Och. 2004. Orange: a
                                                            method for evaluating automatic evaluation metrics
Kyunghyun Cho, Bart Van Merriënboer, Caglar Gul-           for machine translation. In Proceedings of the 20th
  cehre, Dzmitry Bahdanau, Fethi Bougares, Holger           international conference on Computational Linguis-
  Schwenk, and Yoshua Bengio. 2014. Learning                tics, page 501. Association for Computational Lin-
  phrase representations using rnn encoder-decoder          guistics.
  for statistical machine translation. arXiv preprint
  arXiv:1406.1078.                                        Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
                                                            dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Kevin Clark, Minh-Thang Luong, Quoc V. Le, and              Luke Zettlemoyer, and Veselin Stoyanov. 2019.
  Christopher D. Manning. 2020. {ELECTRA}: Pre-             Roberta: A robustly optimized bert pretraining ap-
  training text encoders as discriminators rather than      proach. arXiv preprint arXiv:1907.11692.
  generators. In International Conference on Learn-
  ing Representations.                                    Jiasen Lu, Dhruv Batra, Devi Parikh, and Stefan
                                                             Lee. 2019. Vilbert: Pretraining task-agnostic visi-
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and                olinguistic representations for vision-and-language
   Kristina Toutanova. 2018. Bert: Pre-training of deep      tasks. In Advances in Neural Information Process-
   bidirectional transformers for language understand-       ing Systems, pages 13–23.
   ing. arXiv preprint arXiv:1810.04805.
                                                          Bhaskar Mitra, Nick Craswell, et al. 2018. An intro-
Xiaodong Gu, Hongyu Zhang, and Sunghun Kim. 2018.           duction to neural information retrieval. Foundations
  Deep code search. In 2018 IEEE/ACM 40th Interna-          and Trends R in Information Retrieval, 13(1):1–126.
  tional Conference on Software Engineering (ICSE),
  pages 933–944. IEEE.                                    Matthew E Peters, Mark Neumann, Mohit Iyyer, Matt
                                                           Gardner, Christopher Clark, Kenton Lee, and Luke
Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis       Zettlemoyer. 2018. Deep contextualized word repre-
  Allamanis, and Marc Brockschmidt. 2019. Code-            sentations. arXiv preprint arXiv:1802.05365.
  searchnet challenge: Evaluating the state of seman-
  tic code search. arXiv preprint arXiv:1909.09436.       Fabio Petroni, Tim Rocktäschel, Patrick Lewis, Anton
                                                            Bakhtin, Yuxiang Wu, Alexander H Miller, and Se-
Srinivasan Iyer, Ioannis Konstas, Alvin Cheung, and         bastian Riedel. 2019. Language models as knowl-
   Luke Zettlemoyer. 2016. Summarizing source code          edge bases? arXiv preprint arXiv:1909.01066.
   using a neural attention model. In Proceedings
   of the 54th Annual Meeting of the Association for      Telmo Pires, Eva Schlinger, and Dan Garrette. 2019.
   Computational Linguistics (Volume 1: Long Papers),       How multilingual is multilingual bert?      arXiv
   pages 2073–2083.                                         preprint arXiv:1906.01502.

## Strona 10

Alec Radford, Karthik Narasimhan, Tim Salimans,                 C ODE S EARCH   T RAINING    D EV    T ESTING
  and Ilya Sutskever. 2018. Improving language                  GO               635,635    28,483    14,291
  understanding by generative pre-training. URL                 JAVA             908,886    30,655    26,909
  https://s3-us-west-2. amazonaws. com/openai-                  JAVA S CRIPT     247,773    16,505     6,483
  assets/researchcovers/languageunsupervised/language           PHP             1,047,406   52,029    28,391
  understanding paper. pdf.                                     P YTHON          824,342    46,213    22,176
                                                                RUBY              97,580    4,417      2,279
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine
  Lee, Sharan Narang, Michael Matena, Yanqi Zhou,           Table 6: Data statistics about the CodeSearchNet Cor-
  Wei Li, and Peter J Liu. 2019. Exploring the limits       pus for natural language code search.
  of transfer learning with a unified text-to-text trans-
  former. arXiv preprint arXiv:1910.10683.
                                                            B     Train Details
Alexander M Rush, Sumit Chopra, and Jason We-
  ston. 2015.     A neural attention model for ab-          B.1    Pre-training
  stractive sentence summarization. arXiv preprint
  arXiv:1509.00685.                                         We train CodeBERT on one NVIDIA DGX-2 ma-
                                                            chine using FP16. It combines 16 interconnected
Chen Sun, Austin Myers, Carl Vondrick, Kevin Mur-
  phy, and Cordelia Schmid. 2019. Videobert: A joint        NVIDIA Tesla V100 with 32GB memory. We use
  model for video and language representation learn-        the following set of hyper-parameters to train mod-
  ing. arXiv preprint arXiv:1904.01766.                     els: batchsize is 2,048 and learning rate is 5e-4. We
                                                            use Adam to update the parameters and set the num-
Ilya Sutskever, Oriol Vinyals, and Quoc V Le. 2014.
   Sequence to sequence learning with neural networks.      ber of warmup steps as 10K. We set the max length
   In Advances in neural information processing sys-        as 512 and the max training step is 100K. Training
   tems, pages 3104–3112.                                   1,000 batches of data costs 600 minutes with MLM
                                                            objective, 120 minutes with RTD objective.
Kai Sheng Tai, Richard Socher, and Christopher D
  Manning. 2015. Improved semantic representations
  from tree-structured long short-term memory net-          B.2    CodeSearch
  works. arXiv preprint arXiv:1503.00075.                   In the fine-turning step, we set the learning rate as
Alon Talmor, Yanai Elazar, Yoav Goldberg, and               1e-5, the batch size as 64, the max sequence length
  Jonathan Berant. 2019.     olmpics–on what lan-           as 200 and the max fine-tuning epoch as 8. As the
  guage model pre-training captures. arXiv preprint         same with pre-training, We use Adam to update the
  arXiv:1912.13283.                                         parameters. We choose the model performed best
                                                            on the development set, and use that to evaluate on
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
  Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz             the test set.
  Kaiser, and Illia Polosukhin. 2017. Attention is all
  you need. In Advances in neural information pro-          B.3    Code Summarization on Six
  cessing systems, pages 5998–6008.                                Programming Languages
Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V             We use Transformer with 6 layers, 768 dimensional
  Le, Mohammad Norouzi, Wolfgang Macherey,                  hidden states and 12 attention heads as our decoder
  Maxim Krikun, Yuan Cao, Qin Gao, Klaus
                                                            in all settings. We set the max length of input
  Macherey, et al. 2016. Google’s neural machine
  translation system: Bridging the gap between hu-          and inference as 256 and 64, respectively. We use
  man and machine translation.      arXiv preprint          the Adam optimizer to update model parameters.
  arXiv:1609.08144.                                         The learning rate and the batch size are 5e-5 and
                                                            64, respectively. We tune hyperparameters and
Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Car-
  bonell, Ruslan Salakhutdinov, and Quoc V Le.              perform early stopping on the development set.
  2019. Xlnet: Generalized autoregressive pretrain-
  ing for language understanding. arXiv preprint            B.4    Code Summarization on C#
  arXiv:1906.08237.
                                                            Since state-of-the-art methods use RNN as their de-
A    Data Statistic                                         coder, we choose a 2-layer GRU with an attention
                                                            mechanism as our decoder for a comparison. We
Data statistics of the training/validation/testing data     fine-tune models using a grid search with the fol-
splits for six programming languages are given in           lowing set of hyper-parameters: batchsize is in {32,
Table 6.                                                    64} and learning rate is in {2e-5, 5e-5}. We report

## Strona 11

the number when models achieve best performance
                                                                                                                                                      MODEL                        RUBY      GO
 on the development set.
                                                                                                                                                      RO BERTA                     0.0043   0.0030
 C                              Learning Curve of CodeSearch                                                                                          P RE -T RAIN W / CODE ONLY   0.1648   0.4179
                                                                                                                                                      C ODE BERT                   0.6870   0.8372
 From Figure 4, we can see that CodeBERT per-
                                                                                                                                                  Table 7: Results on natural language code search by
 forms better at the early stage, which reflects that                                                                                             late fusion.
 CodeBERT provides good initialization for learn-
 ing downstream tasks.
                                                                                                                                                  only. And late fusion performs comparable with
                         88.5                    Roberta                                         83.0                    Roberta                  the standard way. What’s more, late fusion is more
                                                 CodeBERT                                                                CodeBERT
                         88.0                    Pre-train w/ code only                                                  Pre-train w/ code only
                                                                                                 82.5                                             efficient and this setting could be used in an online
                         87.5
                                                                                                 82.0                                             system.

Dev Accuracy of Python                                                    Dev Accuracy of Java
                         87.0
                                                                                                 81.5
                         86.5
                                                                                                 81.0                                             E   Case Study
                         86.0
                                                                                                 80.5
                         85.5                                                                                                                     To qualitatively analyze the effectiveness of Code-
                         85.0                                                                    80.0
                                                                                                                                                  BERT, we give some cases for code search and
                         84.5 1   2   3     4    5      6     7     8                            79.5 1   2   3     4    5      6     7     8
                                      The Number of Epoch                                                     The Number of Epoch                 code documentation generation tasks.
                                                                                                                                                     Considering the limited space, we only give the
 Figure 4: Learning curve of different pre-trained mod-
                                                                                                                                                  top2 results of the query for python programming
 els in the fine-tuning step. We show results on Python
 and Java.                                                                                                                                        language. As show in Figure 5, search results are
                                                                                                                                                  very relevant with query.
 D                              Late Fusion                                                                                                          Figure 6 and Figure 7 show the outputs with
                                                                                                                                                  different models for the code documentation gen-
In section §4.1 , we show that CodeBERT per-                                                                                                      eration task. As we can see, CodeBERT performs
forms well in the setting where natural languages                                                                                                 better than all baselines.
and codes have early interactions. Here, we in-
vestigate whether CodeBERT is good at working
as a unified encoder. We apply CodeBERT for
natural language code search in a later fusion set-
ting, where CodeBERT first encodes NL and PL
separately, and then calculates the similarity by dot-
product. In this way, code search is equivalent to
find the nearest codes in the shared vector space.
This scenario also facilitates the use of CodeBERT
in an online system, where the representations of
codes are calculated in advance. In the runtime, a
system only needs to compute the representation
of NL and vector-based dot-product.
   We fine-tune CodeBERT with the following ob-
jective, which maximizes the dot-product of the
ground truth while minimizing the dot-product of
distractors.
                    exp Enc(ci )| Enc(wi )
                                             
      1 X
   −         log P                    | Enc(w )
                                                
     N              j exp   Enc(c  j )        i
         i
                                                  (15)

    Results are given in Table 7. We just do this
 setting on two languages with a relatively small
 amount of data.
    We can see that CodeBERT performs better than
 RoBERTa and the model pre-trained with codes

## Strona 12

Figure 5: Python CodeSearch example. The results are searched from 1,156,085 python code data. We only give
the top2 results because space is limited.




                       Figure 6: Java code documentation generation output example.




                      Figure 7: Python code documentation generation output example.

### Obrazy na stronie

- `image` obiekt 1: ![image strona 12 obiekt 1](pdfimages/codebert/codebert-001.png)
- `smask` obiekt 2: ![smask strona 12 obiekt 2](pdfimages/codebert/codebert-002.png)
- `image` obiekt 3: ![image strona 12 obiekt 3](pdfimages/codebert/codebert-003.png)
- `smask` obiekt 4: ![smask strona 12 obiekt 4](pdfimages/codebert/codebert-004.png)
- `image` obiekt 5: ![image strona 12 obiekt 5](pdfimages/codebert/codebert-005.png)
- `smask` obiekt 6: ![smask strona 12 obiekt 6](pdfimages/codebert/codebert-006.png)

## Strona 13

