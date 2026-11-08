# cvefixes

Źródło: `cvefixes.pdf`

## Strona 1

CVEfixes: Automated Collection of Vulnerabilities and Their
                                                          Fixes from Open-Source Software
                                                           Guru Bhandari                                        Amara Naseer                                   Leon Moonen
                                                   Simula Research Laboratory                            Simula Research Laboratory                     Simula Research Laboratory
                                                          Oslo, Norway                                          Oslo, Norway                                   Oslo, Norway
                                                        guru@simula.no                                       amara@simula.no                            leon.moonen@computer.org

                                         ABSTRACT                                                                          1    INTRODUCTION
                                         Data-driven research on the automated discovery and repair of secu-               The exploitation of security vulnerabilities is a significant threat
                                         rity vulnerabilities in source code requires comprehensive datasets               to the reliability of software systems and to the protection of the




arXiv:2107.08760v1 [cs.SE] 19 Jul 2021
                                         of real-life vulnerable code and their fixes. To assist in such re-               data processed by them, as is frequently evidenced by new data
                                         search, we propose a method to automatically collect and curate a                 leaks, ransomware attacks, and substantial outages of essential
                                         comprehensive vulnerability dataset from Common Vulnerabilities                   systems. Despite the continued efforts of the software engineering
                                         and Exposures (CVE) records in the public National Vulnerability                  community to improve software quality and security by means of
                                         Database (NVD). We implement our approach in a fully automated                    secure coding guidelines, software testing, and various forms of
                                         dataset collection tool and share an initial release of the resulting             code review, the publicly available Common Vulnerabilities and
                                         vulnerability dataset named CVEfixes.                                             Exposures (CVE) records reveal an increasing trend in the number
                                            The CVEfixes collection tool automatically fetches all available               of vulnerabilities that are discovered each year [1].
                                         CVE records from the NVD, gathers the vulnerable code and cor-                        The overall security of software is highly dependent on the ef-
                                         responding fixes from associated open-source repositories, and                    fective and timely identification and mitigation of software vulner-
                                         organizes the collected information in a relational database. More-               abilities. However, this is not an easy task and requires experience
                                         over, the dataset is enriched with meta-data such as programming                  and specialized skills that go beyond the expertise of the typical
                                         language, and detailed code and security metrics at five levels of                developer, resulting in many vulnerabilities that go unnoticed for
                                         abstraction. The collection can easily be repeated to keep up-to-                 a long time. Consequently, there has been considerable attention
                                         date with newly discovered or patched vulnerabilities. The initial                in academia and industry to the development of techniques and
                                         release of CVEfixes spans all published CVEs up to 9 June 2021,                   tools that can help developers identify, and possibly repair, security
                                         covering 5365 CVE records for 1754 open-source projects that were                 vulnerabilities in source code already in the development phase.
                                         addressed in a total of 5495 vulnerability fixing commits.                            Data-driven vulnerability research depends on the availability of
                                            CVEfixes supports various types of data-driven software security               datasets with samples of real-life vulnerable code and their fixes [2].
                                         research, such as vulnerability prediction, vulnerability classifica-             Moreover, such datasets should encompass multiple levels of gran-
                                         tion, vulnerability severity prediction, analysis of vulnerability-               ularity [3, 4], such as files, classes, functions, etc., and cover widely-
                                         related code changes, and automated vulnerability repair.                         used programming languages [5, 6]. Finally, for reliable training and
                                                                                                                           evaluation of machine learning (ML) approaches, we need compre-
                                         CCS CONCEPTS                                                                      hensive datasets that contain large numbers of diverse and labeled
                                         • Security and privacy → Software and application security;                       samples of both vulnerable and non-vulnerable code [7–9]. As we
                                         Vulnerability management; • Software and its engineering →                        will see in the discussion of related work (Section 2), the currently
                                         Software defect analysis; Software libraries and repositories.                    available vulnerability datasets do not fulfill these requirements.
                                                                                                                               To address their shortcomings and assist in data-driven vulner-
                                         KEYWORDS                                                                          ability research, we propose to automatically collect and curate
                                                                                                                           a comprehensive vulnerability dataset from CVE records in the
                                         Security vulnerabilities, dataset, software repository mining, vul-
                                                                                                                           National Vulnerability Database (NVD). In particular, we propose
                                         nerability prediction, vulnerability classification, source code repair.
                                                                                                                           an approach that mines CVE records for open-source software
                                         ACM Reference Format:                                                             (OSS) projects hosted on GitHub, GitLab, and Bitbucket, to collect
                                         Guru Bhandari, Amara Naseer, and Leon Moonen. 2021. CVEfixes: Au-                 real-world samples of vulnerable and corresponding patched code.
                                         tomated Collection of Vulnerabilities and Their Fixes from Open-Source
                                                                                                                           We implement the proposed approach in a dataset collection tool
                                         Software. In Proceedings of the 17th International Conference on Predic-
                                                                                                                           and share an initial release of the resulting vulnerability dataset
                                         tive Models and Data Analytics in Software Engineering (PROMISE ’21),
                                         August 19–20, 2021, Athens, Greece. ACM, New York, NY, USA, 10 pages.             named CVEfixes. The dataset supports various types of data-driven
                                         https://doi.org/10.1145/3475960.3475985                                           software security research, such as ML-based vulnerability iden-
                                                                                                                           tification, automated classification of identified vulnerabilities in
                                                              This work is licensed under a Creative Commons Attribution   Common Weakness Enumeration (CWE) types, vulnerability sever-
                                                              4.0 International (CC BY 4.0) license.                       ity prediction, and automated repair of security vulnerabilities.
                                         PROMISE ’21, August 19–20, 2021, Athens, Greece                                   Contributions: This paper makes the following contributions:
                                         © 2021 Copyright held by the owner/author(s).                                         (a) We survey existing security vulnerability-related datasets
                                         ACM ISBN 978-1-4503-8680-7/21/08.                                                         and discuss their strengths and weaknesses.
                                         https://doi.org/10.1145/3475960.3475985

## Strona 2

PROMISE ’21, August 19–20, 2021, Athens, Greece                                                                  Guru Bhandari, Amara Naseer, and Leon Moonen


   (b) We propose a method to automatically collect and curate a              Flawfinder) as vulnerable or not, classified in five groups of vul-
       comprehensive vulnerability dataset from CVE records in                nerabilities, namely CWE-120, 119, 469, 476, and other. However,
       the NVD, and obtain real-world samples of vulnerable and               there are some challenges with the dataset, such as the fact that it
       corresponding patched code, organized at multiple levels               is highly imbalanced with only 6.8% functions labeled as vulner-
       of granularity. In addition, we discuss how to enrich this             able. Moreover, the extracted functions are incomplete, missing
       data with meta-data such as programming language used,                 the function’s return type which excludes certain (signature-based)
       and detailed code-related metrics at five levels of abstraction,       analyses. SVCP4C (SonarCloud Vulnerable Code Prospector for C)
       such as the commit-, file-, and method levels, as well as the          is an online tool for collecting vulnerable source code from open-
       repository- and CVE levels.                                            source repositories linked to SonarCloud. The tool performs static
   (c) We implement the proposed approach in a dataset collection             analysis and labels the potentially vulnerable source code at the
       tool that is made publicly available.1                                 file level [20]. The Devign [21] dataset includes four real-world
   (d) We publicly share a version of the CVEfixes vulnerability              open-source C/C++ projects, Linux, FFmpeg, Qemu and Wireshark,
       dataset for use by other researchers.2 The initial release spans       where the labeling is performed using security-related keyword
       all published CVE records up to 9 June 2021, covering 5365             filtering. The drawback of this dataset is also in the labeling: if a
       CVE records for 1754 OSS projects. A total of 5495 vulnera-            commit is believed to be vulnerable, then all functions changed
       bility fixing commits are obtained from the projects’ version          by the commit are labeled as vulnerable, which is always not true.
       control systems and linked to information from the corre-              Moreover, the dataset does not classify the types of vulnerabilities
       sponding CVE records, such as CVE-IDs, reference links,                encountered. A threat recognized by the authors of these datasets/-
       severity scores, vulnerability type/CWE type, and other de-            tools is that the labeling is based on static analysis, which is known
       scriptive information.                                                 for its false positives, that may lead to incorrect labeling. Our ap-
The remainder of the paper is organized as follows: Section 2 dis-            proach, as well as others discussed below, aims to mitigate this
cusses the currently available vulnerability datasets and how our             threat by building on actual security patches. The Code Gadget
work differs from them. Section 3 presents the process for construct-         Database (CGD) [22] collects two types of vulnerabilities in C/C++
ing the CVEfixes dataset, followed by an exploration of the initial           programs: buffer error vulnerability (CWE-119) and resource man-
release in Section 4. Section 5 discusses applications of the dataset,        agement error vulnerability (CWE-399). The dataset covers 61638
together with current limitations and future extensions. Finally, we          code gadgets including 17725 vulnerable and 43913 non-vulnerable
conclude in Section 6.                                                        code gadgets. It aims to improve the labeling quality by checking
                                                                              if the code slice of confirmed bugs overlaps with a bug fix before
2    RELATED WORK                                                             labeling code as ’buggy’. Recently, Zheng et al. [17] published D2A,
Several vulnerability-related test suites and datasets were developed         which uses an approach based on differential analysis to label issues
in the last decade, often with particular goals in mind. These sets           in the source code functions or snippets reported by static analysis
were consequently picked up by other security researchers looking             tools. The D2A approach analyzes the commit messages to identify
for relevant data to train or evaluate their techniques on. This              the likeliness of vulnerability fixes from before-commit and after-
section surveys frequently used datasets and discusses some of the            commit versions. The dataset considers code from six open-source
challenges for their reuse in other contexts. We also look at more            C/C++ projects: OpenSSL, FFmpeg, httpd, NGINX, libtiff, and libav.
general software repositories and repository mining frameworks.                   Vieira et al. [23] introduced a dataset of bug-fixing activities from
Finally, we discuss how the CVEfixes dataset is different from the            70000 bug-fixing reports from 10 years of 55 open-source projects
existing work in this area.                                                   of Apache mined from Jira,3 a popular issue tracking system that
Vulnerability Datasets The Software Assurance Metrics And Tool                captures information about software development, bugs, security
Evaluation (SAMATE) project created the Juliet Test Suite as a                vulnerabilities, new functionalities, etc. The dataset’s emphasis is
benchmark for static analysis tools that aim to identify vulnerabil-          on process-related information regarding issue management, such
ities in source code [10, 11]. Programs from the Juliet Test Suite            as change metrics, fix effort, status, version, and assignee, but it
have been used in several studies on vulnerability and weakness               does not go into code-level detail. Alves et al. [24] analyze the
prediction [12–16]. However, the benchmark was never created for              bug-tracking systems of five open-source projects (Mozilla, Linux
this purpose, and concerns have been raised that the vulnerabilities          Kernel, Xen Hypervisor, Httpd, and Glibc), looking for occurrences
in Juliet are not very diverse, and many of them are of a synthetic           of CVE identifiers. They found 2875 security patches and used
nature that does not occur in real-world software projects [2, 17].           the associated code to build a dataset that labels the code before
    Mitropoulus et al. [18] constructed a vulnerability dataset by ana-       patching as vulnerable, and after patching as not vulnerable, as
lyzing the Maven repository using FindBugs [19], a tool conducting            well as adding labels for vulnerability types and severity. Moreover,
static code analysis on Java byte-code, identifying the vulnera-              they compute software metrics at the file, class, and function level
bilities in Maven and categorizing them into nine different types.            for the code before and after patching to enable metrics-based
Similarly, Draper’s VDISC dataset [7] consists of C/C++ source code           vulnerability prediction research. Similarly, Gkortzis et al. [25]
of 1.27 million functions mined from open-source projects that were           present a vulnerability dataset correlating source code and software
labeled by three static code analysis tools (Clang, Cppcheck, and             metrics of 8694 versions of open-source projects.

1 https://github.com/secureIT-project/CVEfixes, doi:10.5281/zenodo.5111494.
2 https://zenodo.org/record/4476563, doi:10.5281/zenodo.4476563.              3 https://atlassian.com/software/jira

## Strona 3

CVEfixes: Automated Collection of Vulnerabilities and Their Fixes from Open-Source Software                                PROMISE ’21, August 19–20, 2021, Athens, Greece


    Jimenez et al. [26] present VulData7, a framework to collect a                      covers more information about the vulnerability at different levels
security vulnerability dataset covering all reported NVD vulnera-                       of granularity, up to the actual source code before and after fixing.
bilities of four security-critical open-source systems, Linux Kernel,                   (2) It covers a longer timeframe, being based on all CVE records
WireShark, OpenSSL, and SystemD. Although focusing on a limited                         available at the collection date of 9 June 2021. Moreover, it’s not
set of systems all written in the C programming language, their                         restricted to this timeframe: at any point in the future, our publicly
approach shares several characteristics with ours, but one main                         available tool can automatically collect and integrate the data up to
practical challenge for reusing their framework is that it is based                     the last published CVE at that point in time. (3) Unlike many other
on the analysis of XML files, a format that is no longer provided                       datasets that focus on specific programming languages like Java or
by the NVD. Similarly, Ponta et al. [27] curated a dataset of 1282                      C/C++, our dataset covers multiple programming languages and
commit fixes to vulnerabilities from 205 open-source Java projects                      allows the language as a query attribute. (4) Some of the existing
obtained from NVD and project-specific web resources, and Fan                           vulnerability datasets only classify the source code as vulnerable or
and Nguyen [28] curated a C/C++ code vulnerability dataset named                        not. In addition to this binary classification, CVEfixes classifies the
Big-Vul that corresponds with code changes and CVE database                             vulnerabilities into categories as defined by Common Weakness
entries from 2002 to 2019.                                                              Enumeration (CWE) types, as well as CVSS severity scores, enabling
    Lin et al. [9] emphasize the need for a benchmark for evaluating                    research into multi-class vulnerability prediction.
the effectiveness of ML approaches aimed at fixing security vulnera-
bility in source code. The authors propose a benchmark dataset that                      3 DATASET CONSTRUCTION
offers labels at two levels of granularity, i.e., the file- and method
level, collected from nine software projects written in the C pro-
                                                                                         3.1 Overall Workflow
gramming language [29]. The challenge with using this dataset for                       The National Vulnerability Database (NVD) [33] is a repository
training purposes is that it contains only 1471 vulnerable functions                    of vulnerability management data maintained by the National In-
and 1320 vulnerable files, which is rather small for training a deep                    stitute of Standards and Technology (NIST). NIST publishes the
learning model.                                                                         entire NVD database for public use employing various data feeds,
Software Repositories and Repository Mining Frameworks                                  including JSON vulnerability feeds, security checklist references,
Ma et al. [30] present World of Code (WoC), a large and frequently                      security-related software flaws, misconfigurations, product names,
updated collection of git-based version control data. The data is                       and impact metrics. The JSON vulnerability feed comprises a daily
indexed three storage abstractions and arranged in four layers. New                     updated feed of vulnerability records (CVEs), organized by year of
and updated repositories are periodically analyzed, and the data-                       origin (updates may concern CVEs published in earlier years).
base is updated once a month. The dataset stores four types of raw                         Each vulnerability in the file has its CVE-ID, publish date, descrip-
git objects: commits, trees, blobs and tags. The bulk extraction of                     tion, associate reference links, vulnerable product configuration,
these raw git objects was done in parallel using libgit2, a portable                    CWE weakness categorization [34], and other metrics. Moreover,
tool implemented in C. Querying this database can help answer                           each vulnerability’s severity is ranked using the Common Vulnera-
different research questions, such as trends in programming lan-                        bility Scoring System (CVSS) [35]. The CVSS is composed of a set of
guages used, ecosystem comparisons, bug prediction, developer                           metrics in three groups, i.e., base, temporal, and environmental, to
migration studies, bot detection, understanding developer trajecto-                     specify the characteristics and contextual information of a vulnera-
ries, etc. In the same way, the dataset can be inspected for different                  bility. There are two versions of the scoring system: CVSSv2 and
security-related research areas, vulnerable commits classification,                     CVSSv3 , that are both in active use in the NVD.5 CVSSv3 introduces
developers’ tendency towards vulnerability, etc.                                        a number of changes over CVSSv2 to score vulnerabilities more
    Perceval [31] is an automatic and incremental data gathering                        accurately and provide more information to distinguish between
tool to mine software development data from various sources such                        different types of vulnerabilities. Finally, when a vulnerability in
as versioning systems, bug tracking systems and mailing lists. The                      an open-source project is fixed, the CVE record will be updated
JSON output of the tool stores commit-level information of the                          with one or more pointers to the relevant source code repositories,
repositories that can be used to analyze the activities of the reposi-                  as well as commit hashes of the fixes. These comprehensive, scru-
tories and the developers. However, the tool does not expose access                     tinized, and frequently updated JSON vulnerability feeds are the
to the finer granularity levels of open-source projects, such as the                    primary basis for generating the vulnerability data in CVEfixes.
code-level vulnerability information that we are concerned with.                           Figure 1 presents the overall workflow of the dataset collection
    PyDriller 4 is a Python package to mine code-level information                      process. It starts by collecting CVE records via JSON vulnerability
from different version control systems [32]. It allows extracting                       feeds. Since these CVE vulnerabilities are categorized according to
commit-, file-, method levels information from git repositories, and                    CWE weakness types [34], we also collect the details of these CWE
it collects all relevant meta-information, including the computation                    types and cross-reference them with the appropriate CVE records.
of a number of code-level metrics. Because of these features, we                           Moreover, for CVEs that have fixes associated with them, the
use PyDriller during the construction of CVEfixes, before mapping                       corresponding open-source project repositories are (temporarily)
the collected data to a relational database.                                            locally cloned, and source-level information about the vulnerable
Differences The CVEfixes dataset presented in this paper differs                        code and the corresponding fixes is gathered based on the commit
from the existing datasets in the following ways: (1) In general, it                    hashes reported in the CVE record. After extracting the vulnerable

4 https://github.com/ishepard/pydriller                                                  5 https://nvd.nist.gov/vuln-metrics/cvss

## Strona 4

PROMISE ’21, August 19–20, 2021, Athens, Greece                                                                             Guru Bhandari, Amara Naseer, and Leon Moonen


                                                                                          MITRE,7 and does not distinguish between individual CWEs and
            associated                                                                    CWE categories, referring to either as “CWE-<num>”. Moreover,
              project
           repositories                                                                   two additional classifications, “NVD-CWE-noinfo” and “NVD-CWE-
                               Bitbucket         GitHub          Gitlab                   other”, are used to refer to cases where, respectively, there is not
                                                                                          enough info for classification, or where the NVD deviates from the
                                              extract fixing                              full CWE. Note that we also found around 250 cases where the NVD
                                                commits
                                                                  commits
                                                                                          feeds contain the CWE classification “unknown”. For consistency,
                                                                                          we map these “unknowns” to “NVD-CWE-noinfo” in our dataset.
                                                 collect                                  Meta-Information for Repositories: At the time of writing, the
                                           vulnerable projects
                                                                                          majority (>80%) of fixes in the NVD refer to code on one of the
                                                                          vulnerability
                                                                           database       three major OSS forges, GitHub, GitLab, and Bitbucket, with 98% of
                                                 update                    (SQLite3)      those being on GitHub. The remaining 20% of fixes point to other
                                              vulnerability
                          records             information                                 forges (e.g., sourceforge or the defunct gitorious), or to project-
                                                                                          specific servers hosting other versioning systems (e.g., mercurial,
             Figure 1: Dataset construction workflow                                      subversion, or CVS). As a result, we focus on gathering code from
                                                                                          those three OSS forges, and we have modeled the repository table
                                                                                          to maximally cover GitHub’s repository meta-information, such
and fixed code, a number of code-level metrics are computed, and                          as repository name, description, date of creation, last date of push,
additional meta-data such as the programming language is derived.                         homepage, programming language, number of forks and number
Finally, the collected information is stored in a relational database.                    of stars. This information can be used to, for example, focus on
   The overall structure of the database is shown in Figure 2. The                        certain programming languages or filter for popular repositories
main tables capture information about CVE records, CWE records,                           by setting a minimum threshold on the number of stars. The latter
OSS repositories, commits, changed files, and changed methods.                            is also a common and effective approach to focus on information
Two additional tables respectively associate fixes with CVEs, and                         related to mature projects. Note that GitLab and Bitbucket do not
CWE classifications with CVEs.                                                            offer all of these attributes, so clearly distinguishable values are
                                                                                          used to represent missing information, such as the value “-1” for the
3.2     Details of the Automated Collection Tool                                          stars_count of Bitbucket repositories (which does not offer stars).
The proposed process has been implemented in a fully automated                            Extraction of Commits: Whenever an OSS vulnerability is fixed,
CVEfixes collection tool, and the remainder of this section discusses                     the reference_json in the CVE record contains the repository URL,
the major phases implemented in the tool. The collection can easily                       as well as a pointer to the exact commit that introduced the fix,
be repeated to keep up-to-date with newly discovered or patched                           by means of a git hash. We use this information to locally (and
vulnerabilities. Since updates can affect any of the published CVEs,                      temporarily) clone the repository, and use it to extract versions
the collection tool currently revisits all published CVEs to check if                     of the code before and after submitting the fix. We extract this
relevant fixes were added. One direction for future work is enabling                      information at the commit-, file- and method level, where each entry
a more incremental process.                                                               in the commits table is associated to one or more cves via the fixes
Scanning of CVE Records: By default, the collection tool retrieves                        table. In addition, the commits table stores meta-information about
all published JSON vulnerability feeds from the NVD server, cover-                        the commit, such as the author, time and date, commit message,
ing the first published CVE in 2002 up to the last published one on                       if it is a merge commit (often to include pull requests in projects
the date of collection (the feeds are updated daily). The JSON files                      using GitHub Flow), the number of lines added or deleted, and Delta
are then aggregated, flattened, and processed to filter out redun-                        Maintainability Model metrics related to the change [36].
dant information from the CVE records (in the original feeds, some                        Extracting the Modified Files: Every entry in the commits table
fields are repeated at deeper nesting levels). All CVE records that do                    is linked via the commit hash to one or more file_changes that were
not have fixes associated with them in the reference_json field are                       included to fix the vulnerability (or vulnerabilities) associated with
ignored, because gathering corresponding vulnerable or fixed code                         the commit. For each file change, the dataset contains the contents
is not possible for these cases. After processing and filtering the                       of the file before and after making the change, in code_before and
records, various details of the vulnerability such as CVE-ID, pub-                        code_after respectively, as well as the diff of the change in the
lished date, last modified date, reference data, CVSS severity scores,                    format delivered by Git, and a parsed version of this information in
vulnerability impact and scope, exploitability score, are recorded in                     diff_parsed, containing a dictionary of added and deleted lines. In
the cve table.                                                                            addition, several meta-data are collected, such as filename, old and
Classification of Vulnerabilities: As discussed before, CVE                               new path, type of the modification (i.e., added, deleted, modified,
records in the NVD are annotated with CWE vulnerability types                             or renamed), number of lines added or removed in that file, lines
that indicate at a more abstract level what kind of vulnerability                         of code (nloc) after the change, and cyclomatic complexity after
this CVE concerns. The problemtype_json field of the NVD JSON                             the change. Finally, the Guesslang tool8 is used to detect the actual
vulnerability feeds may refer to one or more of these CWE types.                          programming_language that is used in a given file. Guesslang is an
The NVD only uses a subset6 of the full CWE list maintained by
                                                                                          7 https://cwe.mitre.org/data/index.html
6 https://nvd.nist.gov/vuln/categories                                                    8 https://guesslang.readthedocs.io/en/latest/

### Obrazy na stronie

- `image` obiekt 0: ![image strona 4 obiekt 0](pdfimages/cvefixes/cvefixes-000.png)
- `image` obiekt 1: ![image strona 4 obiekt 1](pdfimages/cvefixes/cvefixes-001.png)
- `smask` obiekt 2: ![smask strona 4 obiekt 2](pdfimages/cvefixes/cvefixes-002.png)
- `image` obiekt 3: ![image strona 4 obiekt 3](pdfimages/cvefixes/cvefixes-003.png)
- `image` obiekt 4: ![image strona 4 obiekt 4](pdfimages/cvefixes/cvefixes-004.png)
- `image` obiekt 5: ![image strona 4 obiekt 5](pdfimages/cvefixes/cvefixes-005.png)
- `smask` obiekt 6: ![smask strona 4 obiekt 6](pdfimages/cvefixes/cvefixes-006.png)
- `image` obiekt 7: ![image strona 4 obiekt 7](pdfimages/cvefixes/cvefixes-007.png)
- `smask` obiekt 8: ![smask strona 4 obiekt 8](pdfimages/cvefixes/cvefixes-008.png)

## Strona 5

CVEfixes: Automated Collection of Vulnerabilities and Their Fixes from Open-Source Software                               PROMISE ’21, August 19–20, 2021, Athens, Greece



                 cve                                       fixes                              commits                           repository
                 PK cve_id                                 PK cve_id (FK)                     PK hash                           PK repo_url
                     published_date                        PK hash (FK)                       PK repo_url (FK)                     repo_name
                     last_modified_date                    PK repo_url (FK)                      author                            description
                     description                                                                 author_date                       date_created
                     nodes                                                                       author_timezone                   date_last_push
                     severity                              cwe_classification                    committer                         homepage
                     obtain_all_privilege                  PK cve_id (FK)                        committer_date                    repo_language
                     obtain_user_privilege                                                       committer_timezone                owner
                                                           PK cwe_id (FK)
                     obtain_other_privilege                                                      msg                               forks_count
                     user_interaction_required                                                   merge                             stars_count
                     cvss2_vector_string                   cwe                                   parents
                     cvss2_access_vector                                                         num_lines_added
                                                           PK cwe_id
                     cvss2_access_complexity                                                     num_lines_deleted
                     cvss2_authentication                     cwe_name
                                                                                                 dmm_unit_complexity
                     cvss2_confidentiality_impact             description
                                                                                                 dmm_unit_interfacing
                     cvss2_integrity_impact                   extended_description
                                                              url                                dmm_unit_size
                     cvss2_availability_impact
                     cvss2_base_score                         is_category                                                       method_change
                                                                                              file_change
                     cvss3_vector_string                                                                                        PK method_change_id
                     cvss3_attack_vector                                                      PK file_change_id
                                                                                                                                   file_change_id (FK)
                     cvss3_attack_complexity                                                       hash (FK)
                                                                                                                                   name
                     cvss3_privileges_required                                                     filename
                                                                                                                                   signature
                     cvss3_user_interaction                                                        old_path
                                                                                                                                   parameters
                     cvss3_scope                                                                   new_path
                                                                                                                                   start_line
                     cvss3_confidentiality_impact                                                  change_type
                                                                                                                                   end_line
                     cvss3_integrity_impact                                                        diff
                                                                                                                                   code
                     cvss3_availability_impact                                                     diff_parsed
                                                                                                                                   nloc
                     cvss3_base_score                                                              num_lines_added
                                                                                                                                   complexity
                     cvss3_base_severity                                                           num_lines_deleted
                                                                                                                                   token_count
                     exploitability_score                                                          code_after
                                                                                                                                   top_nesting_level
                     impact_score                                                                  code_before
                                                                                                   nloc                            before_change
                     ac_insuf_info
                     reference_json                                                                complexity
                     problemtype_json                                                              token_count
                                                                                                   programming_language


   Figure 2: Entity-Relationship Diagram showing the various levels of abstraction in CVEfixes and their interconnections


open-source deep-learning based classifier that was trained with                               • sample_limit: an optional limit on the number of commits to
over a million source code files, and recognizes over 30 program-                                be gathered (mainly for testing and demonstration purposes,
ming languages. Note that these detected languages may differ                                    sample_limit = 0 means unlimited collection).
from, and are more precise than the repository language that is, for                     Note that the GitHub API is severely rate-limited when unauthen-
example, reported by GitHub.                                                             ticated access is used. These limits can be raised significantly to up
Extracting the Modified Methods: Similar to the changes at the                           to 5000 requests per hour by authenticatinsg with a username and
file-level, we keep track of changes at the method-level in the                          personal access token.10 A github_username and github_token can
method_change table. In addition to the actual code, each method                         be configured in .CVEfixes.ini for this purpose. With a sample limit
change stores meta-information such as the method name, its sig-                         of 25, no token is needed and rate-limiting will not be triggered.
nature, parameters, start and end line of the method, lines of code,                        We provide a compressed SQL dump for the initial release of the
cyclomatic complexity, and a boolean indicating whether this con-                        CVEfixes vulnerability dataset that covers all published CVEs in the
cerns the code from before committing the fix or not.                                    NVD up to 9 June 2021 at Zenodo.11 The distribution contains a
                                                                                         simple shell script to convert the compressed SQL dump into an
3.3     Practical Guidance                                                               SQLite3 database:
The automated CVEfixes dataset collection tool is distributed via                               $ sh Code / create_CVEfixes_from_dump . sh
GitHub.9 The distribution comes with detailed requirements and
installation instructions. It requires Python3.8 or later to run, and                   Alternatively, the CVEfixes dataset can be gathered from scratch
SQLite3 to construct and store the data into a relational database.                     using the following shell script:
The main Python packages that it depends on are pandas, numpy,                                  sh Code / create_CVEfixes_from_scratch . sh
requests, PyDriller, PyGithub and guesslang. We provide require-
ments.txt and environment.yml files for dependency management                            Note that this process will overwrite an existing database. More-
using pip/venv or anaconda/miniconda.                                                    over, at the time of writing, the full collection process can take up
   The tool is configured by means of a number of settings in a                          to 15 hours, depending on the available internet connection. The
.CVEfixes.ini file (an example is provided in the distribution):                         advantage of taking this route is that the database will contain all
                                                                                         CVEs published up to the date of initiating the collection process.
      • database_path: location of the CVEfixes database file (also
        used to hold some temporary files during extraction).                           10 https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-
                                                                                         access-token
9 https://github.com/secureIT-project/CVEfixes, doi:10.5281/zenodo.5111494.             11 https://zenodo.org/record/4476563, doi:10.5281/zenodo.4476563.

## Strona 6

PROMISE ’21, August 19–20, 2021, Athens, Greece                                                           Guru Bhandari, Amara Naseer, and Leon Moonen


   The distribution contains an example Jupyter Notebook Exam-              Table 2: Top 10 projects in CVEfixes with respect to (a) the
ples/query_CVEfixes.ipynb that shows how to explore the CVEfixes            number of fixed CVEs, shown with the project’s security
dataset and contains the code to generate the various tables and            metrics, (b) number of vulnerability fixing commits, and the
graphs in this paper.                                                       number of (c) files and (d) methods involved in these fixes.
   Recall the overall structure of the database shown in Figure 2.
Then the following query extracts all methods involved in fixes                                      average    average            average        average
related to C programs before the changes were made:                          project     # CVEs      CVSSv2     CVSSv3        exploitability       impact

      SELECT m . name , m . signature , m . nloc , m .                       linux           973        5.30           3.99              1.16         2.78
          parameters , m . token_count , m . code                            ImageMagick     157        5.45           7.25              2.74         4.43
                                                                             tensorflow      143        3.92           6.67              2.05         4.50
      FROM method_change m , file_change f
                                                                             tcpdump          89        7.33           9.57              3.86         5.70
      WHERE f . file_change_id = m . file_change_id
                                                                             FFmpeg           83        6.35           5.86              2.23         3.57
      AND f . programming_language = 'C '                                    phpmyadmin       67        4.46           3.55              1.85         1.53
      AND m . before_change = True                                           php-src          60        6.59           7.46              3.22         4.21
                                                                             MISP             50        5.03           6.70              2.81         3.61
Another example, inspired by the ManySStuBs4J dataset [37], to
                                                                             WordPress        46        5.27           7.01              3.06         3.66
find all files that only add or remove a single line as fix:                 hhvm             40        6.48           7.54              3.22         4.31
      SELECT cv . cve_id , f . filename , f .                                                                    (a)
          num_lines_added , f . num_lines_deleted , f .
          code_before , f . code_after , cc . cwe_id                        project     # commits project              # files project          # methods
      FROM file_change f , commits c , fixes fx , cve
                                                                            linux            1,029   linux       2,007        GeniXCMS              14,235
          cv , cwe_classification cc                                        ImageMagick        171   GeniXCMS    1,930        linux                  4,303
      WHERE f . hash = c . hash AND c . hash = fx . hash                    tensorflow         156   kanboard      698        exponent-cms           3,048
      AND fx . cve_id = cv . cve_id                                         phpmyadmin         126   CycloneTCP    611        Ilch-2.0               1,427
      AND cv . cve_id = cc . cve_id                                         tcpdump            101   X2CRM         594        arangodb               1,224
      AND f . num_lines_added <=1                                           FFmpeg              88   exponent-cms 445         kanboard               1,169
      AND f . num_lines_deleted <=1;                                        php-src             61   Ushahidi-Web 402         tensorflow             1,045
                                                                            MISP                54   wityCMS       372        moped                    950
                                                                            WordPress           47   tcpdump       344        WordPress                915
4    DATASET EXPLORATION                                                    radare2             43   tensorflow    340        X2CRM                    790
Table 1 presents the summary statistics of the initial release of the                  (b)                     (c)                        (d)
CVEfixes dataset. This initial release covers 5365 unique CVEs in
1754 OSS projects, with 5495 unique vulnerability fixing commits.              Looking at the projects in the four top ten lists of Table 2a-2d, it
The CVEs are classified into 180 different CWE vulnerability types.         is not surprising to see some overlap between the lists. On the other
Note that some of the vulnerability fixing commits cover multiple           hand, it is surprising to see that some projects, such as GeniXCMS,
CVEs, as is indicated by the number of commits being lower than             kanboard, and exponent-cms, which do not occur at all in the top ten
the number of CVEs.                                                         CVEs and #commits, come in very highly ranked on the amounts
   To further characterize the data, Table 2 presents the top ten           of files and methods that need to be changed to fix vulnerabilities
projects in CVEfixes with respect to the number of CVEs, number             in these projects. This sudden rise in the ranks suggests it can
of vulnerability fixing commits, and number of files and meth-              be of interest to investigate how the modularization decisions in
ods involved in fixes. In particular, Table 2a corresponds with the         these projects impacted the security fixes that were made, and may
project-wise number of CVEs, the average CVSSv2 and CVSSv3 base             indicate an application-level code smell such as shotgun surgery.
scores of these vulnerabilities, as well as their average exploitability,      This finding also shows that there is no direct correlation be-
and impact scores. Not surprisingly, the long-running and well-             tween the number of files or methods and the number of CVEs (or
scrutinized linux project has the most vulnerabilities and vulner-          commits to fix them), because that would mean the respective top
ability fixing commits (shown in resp. Table 2a and 2b), i.e., 1029         tens would have been similar. We do see the expected relation be-
commits for fixing 973 vulnerabilities. Note that linux has roughly         tween CVEs and vulnerability fixing commits (with minor changes
six times as much vulnerabilities as ImageMagick, the project with          due to some commits covering multiple CVEs, as noted earlier).
second most vulnerabilities (157), yet the security impact of those            The 10 projects in Table 2a cover 31.84% of the total number
discovered in ImageMagick is considerably larger, as shown by the           of CVEs, those in Table 2b cover 31.61% of the total number of
various security metrics.                                                   vulnerability fixing commits, the ones in Table 2c account for 42.43%
                                                                            of the total number of files involved in fixes, and finally, the ten
     Table 1: Summary statistics of the CVEfixes dataset                    projects in Table 2d make up 57.84% of the total number of methods
                                                                            involved in fixes.
      CVEs     CWEs       projects    commits     files    methods             Table 3 presents the ten most occurring CWE types based on
                                                                            CVE count. We see that CWE-79 (Improper Neutralization of Input
      5,365      180        1,754        5,495    18,249    50,322
                                                                            During Web Page Generation, is the most commonly identified

## Strona 7

CVEfixes: Automated Collection of Vulnerabilities and Their Fixes from Open-Source Software                                                                           PROMISE ’21, August 19–20, 2021, Athens, Greece


  Table 3: Distribution of vulnerabilities over CWE types                               Table 5: Average number of days between CVE publication
                                                                                        and vulnerability fix for the top ten projects with most CVEs
CWE          description                                      CVEs cmts files           (cf. Table 2a).
CWE-79      Improper Neutralization of Input During 635 670 3226
            Web Page Generation (Cross-site Scripting)                                        project                                            # CVEs              # CWEs        min     max     median   mean
CWE-119 Improper Restriction of Operations within 408 403 716
                                                                                              linux                                                          973          53         0    4,582        49   213.64
            the Bounds of a Memory Buffer
                                                                                              ImageMagick                                                    157          27         1    1,474        75   190.14
CWE-20 Improper Input Validation                       382 397 1965
                                                                                              tensorflow                                                     143          24         2      810        16    22.15
CWE-125 Out-of-bounds Read                             380 404 1061
                                                                                              tcpdump                                                         89           4         1      918         1    12.96
CWE-200 Exposure of Sensitive Information to an 276 314 818
                                                                                              FFmpeg                                                          83          17         1    1,523        44    63.22
            Unauthorized Actor
                                                                                              phpmyadmin                                                      67          13         1    1,211        13    36.15
CWE-787 Out-of-bounds Write                            205 211 537
                                                                                              php-src                                                         60          17         3      855        27    50.26
CWE-476 NULL Pointer Dereference                       195 198 334
                                                                                              MISP                                                            50          17         0      430         1    29.33
noinfo*     Insufficient Information                   193 219 664
                                                                                              WordPress                                                       46          14         2      217         4    18.17
other*      Other                                      165 170 395
                                                                                              hhvm                                                            40          18         1    1,328        37   182.18
CWE-264 Permissions Privileges and Access Controls 143 148 457
  * abbreviated from NVD-CVE-noinfo and NVD-CWE-other for space.

                                                                                        or agree on them on a case-by-case basis with the projects. As a re-
vulnerability type. This type is commonly known as Cross-site                           sult of the variability this introduces in the time between disclosure
Scripting or XSS. It has been assigned to 635 CVEs and was fixed                        and publication time, it is impossible to make strong statements on
in 670 commits that changed 3226 files. Observe that the number                         how long the projects really used to address the vulnerability.
of vulnerability fixing commits is larger than the number of CVEs,                         With the above caveat in mind, Table 4 shows some statistics for
which is caused by the fact that some of the CVEs are associated                        the complete CVEfixes dataset on how many days it took from the
with multiple fixes. This occurs, for example, when a CVE is fixed                      CVE publication to committing a fix for the vulnerability. Moreover,
in several related projects, or when the fix is spread over multiple                    Table 5 presents such statistics for the top ten projects with most
commits. On second place comes CWE-119 (Improper Restriction                            CVEs, as earlier presented in Table 2a.
of Operations within the Bounds of a Memory Buffer), reported in                           The last two characteristics that we will investigate are the vul-
408 CVEs and fixed in 403 commits that changed 716 files.                               nerability severity scores of CVEs in CVEfixes, as well as the impact
    Next, we find CWE-20 (Improper Input Validation) assigned to                        that their fixes had on the maintainability of the project by means of
382 CVEs. which is closely followed by CWE-125 (Out-of-bounds                           the delta maintainability model (DMM). The delta maintainability
Read), which is actually a “child” of the more general CWE-119                          model (DMM) [36] is a measure to compare and rank fine-grained
category, and indicates that an index pointer is used beyond the                        code changes into low and high-risk changes. The overall DMM
bounds of the memory buffer. It is reported in 380 CVEs and fixed                       score refers to the proportion of low-risk changes in a commit,
in 404 commits that modified 1159 files. After this top four, we see a                  and is computed as the mean of three individual metrics that re-
considerable drop in the number of CVEs assigned to lower-ranked                        spectively measure the risk associated with code size, (cyclomatic)
CWEs. The top ten CWEs cover approximately 55.58% of the total                          complexity, and size of the interface. The values of each of the DMM
number of CVEs, 57% of the total number of commits, and 55.75%                          metrics range from 0 to 1, with higher values indicating better main-
of the total number of files.                                                           tainability, i.e., lower risk changes, and low values indicating poor
    We also investigated if it was possible to compute how long                         maintainability, i.e., high risk changes.
it took to fix the vulnerabilities, from the day that the CVE was
disclosed to the project to the day that the fix was committed. Un-
fortunately, the NVD only includes the CVE publication date, which
generally does not indicate when the vulnerability was discovered                                                                                            se




                                                                                                    vulnerability severity measures
                                                                                                                                                        ba
or when it was shared with the project. The actual disclosure date                                                                                  2
                                                                                                                                                 SS
can be several months earlier if a responsible disclosure process                                                                           CV
                                                                                                                                        g
                                                                                                                                      av
is used. For example, Google’s Project Zero delays publication for                                                                                      ba
                                                                                                                                                             se
                                                                                                                                                    3
90 days after disclosing vulnerabilities that are not actively being                                                                             SS
                                                                                                                                            CV
                                                                                                                                        g
exploited, giving the option for earlier publication with mutual                                                                      av
                                                                                                                                                            lity
agreement. Other security researchers may use other time frames                                                                                         bi
                                                                                                                                                 o   ita
                                                                                                                                              pl
                                                                                                                                            ex
                                                                                                                                        g
                                                                                                                                      av
                                                                                                                                                                ct
Table 4: Average number of days between CVE publication                                                                                                    pa
                                                                                                                                                     im
                                                                                                                                               g
and vulnerability fix for all CVEs in CVEfixes.                                                                                              av
                                                                                                                                                                      0        2     4       6     8   10
                                                                                                                                                                                    metric score

          mean        std     min      25%     50%      75%      max
                                                                                         Figure 3: Violin plot showing the distribution of average vul-
          171.55    414.93      0      7.0     28.0   123.25     7,636                   nerability severity scores for projects included in CVEfixes

## Strona 8

PROMISE ’21, August 19–20, 2021, Athens, Greece                                                                                                      Guru Bhandari, Amara Naseer, and Leon Moonen


                                                                                                                         Automated Vulnerability Prediction/Identification The CVE-
                                                                                                                         fixes dataset contains different levels of vulnerability data, such as
                                                                              e
                                                                        siz                                              CVE-ID, version, description, type, publication date, current status,
                                                                   it




      delta maintainability metrics
                                                               un
                                                av
                                                         g                                                               all interlinked up to the actual code changes that were introduced to
                                                                          ity
                                                                                                                         fix the vulnerability. This data can be used to extract code features
                                                                        ex
                                                                pl                                                       and metrics that help to better understand how security vulnerabil-
                                                         com
                                                 it                                                                      ities are introduced in code. Moreover, the features and metrics can
                                               un
                                        g
                                      av                                      g                                          be used to model, train, and test vulnerability predictors based on
                                                                  cin
                                                               rfa
                                                    i   ti
                                                           n te                                                          classical machine learning approaches, and the textual descriptions,
                                               un
                                      av
                                           g                                                                             ranging from the CVE vulnerability level to the code level, can be
                                                                             e
                                                                         or
                                                               M
                                                                    sc                                                   used to train deep learning-based models for vulnerability predic-
                                                        DM                                                               tion. Many studies have already targeted automated vulnerability
                                                g                                 0.0   0.2    0.4    0.6    0.8   1.0
                                           av
                                                                                              metric score               identification using various machine learning models [7, 38–40],
                                                                                                                         and Section 2 surveyed some of the challenges with the datasets
Figure 4: Violin plot showing the distribution of average                                                                used in these studies, such as limited size, lack of representative-
DMM scores for fixes to the projects included in CVEfixes                                                                ness, and dataset imbalance. A comprehensive dataset like CVEfixes
                                                                                                                         helps to overcome these challenges and enables a more thorough
                                                                                                                         evaluation of the approaches.
   Figure 3 presents violin plots that show the distribution of CVSSv2                                                   Automated Vulnerability Classification The inclusion of vul-
and CVSSv3 base scores, as well as exploitability and impact, for all                                                    nerability classifications in CVEfixes allows us to go one step further
vulnerabilities in CVEfixes, aggregated into averages per project.                                                       than automated vulnerability prediction, it also enables research on
The width of each violin corresponds to the frequency of data points                                                     automated vulnerability classification, i.e., not just predicting the
with that average. Inside the violin there is small box plot showing                                                     presence of a vulnerability but characterizing the type of the vulner-
the ends of the first and third quartiles, and the median is indicated                                                   ability. Such a classification is of interest since (automated) program
by the white dot. The values of these vulnerability severity metrics                                                     repair approaches may have different efficacy and efficiency for
can vary between 0 and 10, with lower being better, and higher                                                           different vulnerability types, so knowing the vulnerability type
being worse. The figure suggests that the majority of the vulnera-                                                       helps to inform which repair strategy to take. To address this chal-
bilities have severity scores that are on the high side of the severity                                                  lenge, 𝜇VulDeePeaker [4] and ManySStuBs4J [37] have constructed
range, although their exploitability and impact tends to be on the                                                       the multi-class vulnerability dataset. However, those datasets are
lower sides of their respective ranges.                                                                                  specific to a given programming language and certain vulnerabil-
   Figure 4 presents violin plots that show the distribution of DMM                                                      ity/bug types. CVEfixes, on the other hand, uses the well-known
metrics of all vulnerability fixing commits in CVEfixes, again ag-                                                       CWE taxonomy to classify vulnerabilities in a hierarchy of vulner-
gregated into averages per project. These metrics show how the                                                           ability types and categories, and covers 27 programming languages
maintainability of the projects was affected by the security fixes.                                                      (though 9 of these have fewer than 100 files changed in the commits
Observe that the individual DMM metrics unit size, unit complexity,                                                      covered by the dataset).
and unit interfacing mostly have a high density around 0 (indicating                                                     Analysis of vulnerability fixing patches Similar to how the vul-
high risk changes with a detrimental effect on maintainability), and                                                     nerable code in CVEfixes can be used to better understand how
a smaller number of changes are considered low risk (with scores                                                         security vulnerabilities are introduced in code and how these can
closer to 1). The overall DMM score is an aggregate computed as the                                                      be automatically predicted, the fixes offered by CVEfixes can be
mean of the individual metrics [36]. As such, it is more universally                                                     used to analyze and build on vulnerability fixing patches. Several
spread across different risk values, but still with a considerable                                                       studies have already initiated research analyzing such patches, such
number of commits requiring high-risk code change to fix the vul-                                                        as the detection of patterns that can be used in automated program
nerabilities, with the median around 0.25 and the third quartile                                                         repair [41], and the identification of security-relevant commits, also
around 0.6. An interesting question for follow-up research is inves-                                                     known as pre-patches, as these may inadvertently leak information
tigating if vulnerability fixing commits that lower maintainability                                                      about security vulnerabilities before the CVE is published [42, 43].
are followed by refactoring commits that restore maintainability.                                                        Other research has analyzed vulnerability fixing patches to facilitate
                                                                                                                         the automated transformation of patches into “honeypots” that help
5 DISCUSSION                                                                                                             trap malicious actors and detect if the corresponding vulnerabilities
                                                                                                                         are exploited in the wild [44].
5.1 Applications of CVEfixes                                                                                             Automated program repair The pairs of vulnerable and fixed
The CVEfixes dataset can be used in several ways to support data-                                                        code provided by CVEfixes can be used to train machine learning-
driven software security research, for example, for automated vul-                                                       based automated program repair along the lines of SequenceR [45]
nerability prediction, automated classification of identified vulner-                                                    and related work surveyed in Section 2, though we need to warn for
abilities in Common Weakness Enumeration (CWE) types, vul-                                                               a caveat w.r.t. the completeness of the patches, as discussed in more
nerability severity prediction, and automated repair of security                                                         detail in the next section. Moreover, the current state of the art in
vulnerabilities. The remainder of this section discusses several of                                                      this area is constrained with respect to the length of repairs that can
these applications in more detail.                                                                                       be learned/synthesized, with 50 tokens being mentioned as an upper

## Strona 9

CVEfixes: Automated Collection of Vulnerabilities and Their Fixes from Open-Source Software                              PROMISE ’21, August 19–20, 2021, Athens, Greece


limit for acceptable performance [46]. By querying into CVEfixes                         6      CONCLUDING REMARKS
data as shown in the previous subsection (and the example Jupyter                        In this study, we propose the CVEfixes dataset and a fully automated
Notebook in the distribution), CVEfixes facilitates the extraction of                    collection tool that fetches this vulnerability dataset from publicly
specific fixes that used only single (or a few) modified lines for fixing                available information in the NVD and different version control sys-
a vulnerability. This can be used to focus attention of the training                     tems. The dataset consists of real-world samples of vulnerable and
process on cases with a lower number of modified tokens which                            corresponding patched code, their security metrics at five levels of
are within reach of the technology, in order to help improve patch                       abstraction, all linked to the CVE records. The collected informa-
quality. Several studies [47–50] have already initiated work on the                      tion is enriched with various security and code related metrics and
prediction of bugs/errors taking single line modified statements into                    organized into a relational database to support easy querying.
account using the ManySStuBs4J dataset [37]. Querying CVEfixes                              The initial release of the dataset covers 5495 vulnerability fix-
in the way we presented earlier enables the extension of this work                       ing commits from 1754 open-source projects. This multi-level
towards different programming languages, and vulnerability types.                        dataset establishes both qualitative and quantitative opportuni-
                                                                                         ties for vulnerability-related investigations. Researchers can study
                                                                                         the relation from published CVEs all the way down to the corre-
5.2     Limitations and Future Extensions
                                                                                         sponding code level vulnerabilities and their proposed fixes. The
One of the limitations of the current CVEfixes collection tool is                        CVEfixes dataset enables research on vulnerability detection and
that it collects all available fixes from scratch. We opted for this                     classification, vulnerability severity prediction, (pre-)patch anal-
approach since any of the CVEs in the NVD may receive updates, so                        ysis, automated vulnerability repair, and many others. We plan
all should be inspected anyway. Nevertheless, it may be interesting                      to periodically update CVEfixes, and extend it with mining other
to explore a more incremental update scheme that only clones a                           open-source projects from different version control systems and
repository if not all of its fixes are already captured in the database,                 issue tracking systems.
and augments the existing fixes in the other case. Such an approach
would help to speed up the process of updating the database. One                         ACKNOWLEDGMENTS
caveat is that we may also need to remove fixes from the database if
                                                                                        The work presented in this paper has been financially supported
they are no longer referenced by a CVE, but as we have seen, those
                                                                                        by the Research Council of Norway through the secureIT project
fixes may be referred to by other CVEs as well, so some additional
                                                                                        (RCN contract #288787).
checks would be needed.
    Another challenge/limitation that we have noticed is that some                       REFERENCES
of the project repositories referenced in the NVD are no longer
                                                                                          [1]   MITRE. Common Vulnerabilities and Exposures (CVE). url: https:
available. There can be multiple reasons; for example, the owners
                                                                                                //cve.mitre.org/ (visited on May 28, 2021).
might have removed/changed/renamed their repositories, or they                            [2]   M.-j. Choi, S. Jeong, H. Oh, and J. Choo. “End-to-End Prediction of
may have moved the repository between forges. This makes it                                     Buffer Overruns from Raw Source Code via Neural Memory Net-
impossible to fetch the fixes for these repositories. The current                               works.” In: Int’l Joint Conf. Artificial Intelligence. 2017, pp. 1546–1553.
implementation tries to gather code from as many repositories as                          [3]   P. Morrison, K. Herzig, B. Murphy, and L. Williams. “Challenges with
possible, and removes references to those that are unavailable to                               Applying Vulnerability Prediction Models.” In: Symp. and Bootcamp
present an internally consistent view. However, this choice also                                on the Science of Security. ACM, 2015, pp. 1–9.
means that we only present a subset of the information that is                            [4]   D. Zou, S. Wang, S. Xu, Z. Li, and H. Jin. “𝜇VulDeePecker: A Deep
available in the NVD.                                                                           Learning-Based System for Multiclass Vulnerability Detection.” In:
                                                                                                IEEE Trans. Dependable and Secure Computing (2019), p. 13.
    A last limitation is that a commit that is referenced as a vul-
                                                                                          [5]   X. Wang, K. Sun, A. Batcheller, and S. Jajodia. “Detecting "0-Day"
nerability fixing commit in the NVD can still leave (part of) the
                                                                                                Vulnerability: An Empirical Study of Secret Security Patch in OSS.”
vulnerability in the source code, and there may be later commits                                In: Int’l Conf. Dependable Systems and Networks. 2019, pp. 485–492.
that complete the fix of the vulnerability, or the commit may contain                     [6]   Z. Feng et al. “CodeBERT: A Pre-Trained Model for Programming and
changes unrelated to the fix [51]. To further improve the quality of                            Natural Languages.” In: Findings of the Association for Computational
the data, it would be of interest for future work to analyze consecu-                           Linguistics: EMNLP 2020. 2020, pp. 1536–1547.
tive patches, and select/untangle the code that together addresses                        [7]   R. Russell, L. Kim, L. Hamilton, T. Lazovich, J. Harer, O. Ozdemir, P.
the vulnerability.                                                                              Ellingwood, and M. McConley. “Automated Vulnerability Detection
    Another direction for future work is upgrading our extraction                               in Source Code Using Deep Representation Learning.” In: Int’l Conf.
tool to support mining the repositories from other issue-tracking                               Machine Learning and Applic. IEEE, 2018, pp. 757–762.
                                                                                          [8]   R. Coulter, Q.-L. Han, L. Pan, J. Zhang, and Y. Xiang. “Code Anal-
and version control systems, i.e., Bugzilla, Mercurial, Subversion,
                                                                                                ysis for Intelligent Cyber Systems: A Data-Driven Approach.” In:
etc. This will make it possible to gather vulnerability data from an
                                                                                                Information Sciences 524 (2020), pp. 46–58.
even larger collection of projects.                                                       [9]   G. Lin, S. Wen, Q.-L. Han, J. Zhang, and Y. Xiang. “Software Vul-
    Finally, considering the current controversy around ML models                               nerability Detection Using Deep Neural Networks: A Survey.” In:
that are trained on (A)GPL licensed code and may possibly regurgi-                              Proceedings of the IEEE (2020), pp. 1–24.
tate some of that code as part of their operation, we plan to extend                     [10]   T. Boland and P. E. Black. “Juliet 1.1 C/C++ and Java Test Suite.” In:
our datamodel with license information for the fixes included, so                               IEEE Computer 45.10 (2012), pp. 88–90.
that users of CVEfixes can make an informed choice about including                       [11]   P. E. Black. “A Software Assurance Reference Dataset: Thousands of
or excluding certain fixes from their training data.                                            Programs With Known Bugs.” In: 123 (2018).

## Strona 10

PROMISE ’21, August 19–20, 2021, Athens, Greece                                                                     Guru Bhandari, Amara Naseer, and Leon Moonen


[12]   M. Gupta, M. Govil, and G. Singh. “Text-Mining and Pattern-Matching            [31]   S. Dueñas, V. Cosentino, G. Robles, and J. M. Gonzalez-Barahona.
       Based Prediction Models for Detecting Vulnerable Files in Web Ap-                     “Perceval: Software Project Data at Your Will.” In: Int’l Conf. Softw.
       plications.” In: J. Web Eng. 17.1-2 (2018), pp. 28–44.                                Eng. ACM, 2018, pp. 1–4.
[13]   M. K. Gupta, M. C. Govil, and G. Singh. “Predicting Cross-Site Script-         [32]   D. Spadini, M. Aniche, and A. Bacchelli. “PyDriller: Python Frame-
       ing (XSS) Security Vulnerabilities in Web Applications.” In: Int’l Joint              work for Mining Software Repositories.” In: Joint European Softw.
       Conf. Computer Science and Softw. Eng. 2015, pp. 162–167.                             Eng. Conf. and Symp. Found. Softw. Eng. ACM, 2018, pp. 908–911.
[14]   S. A. Mokhov, J. Paquet, and M. Debbabi. “MARFCAT: Fast Code                   [33]   NIST. National Vulnerability Database (NVD). url: https://nvd.nist.
       Analysis for Defects and Vulnerabilities.” In: Int’l Ws. Softw. Analytics.            gov/ (visited on July 22, 2020).
       2015, pp. 35–38.                                                               [34]   MITRE. Common Weakness Enumeration (CWE). url: https://cwe.
[15]   I. Medeiros, N. F. Neves, and M. Correia. “Automatic Detection and                    mitre.org/ (visited on May 28, 2021).
       Correction of Web Application Vulnerabilities Using Data Mining to             [35]   Forum of Incident Response and Security Teams (FIRST). Common
       Predict False Positives.” In: Int’l Conf. World Wide Web. ACM, 2014,                  Vulnerability Scoring System (CVSS). url: https://www.first.org/cvss
       pp. 63–74.                                                                            (visited on May 28, 2021).
[16]   S. Mokhov, J. Paquet, and M. Debbabi. “The Use of NLP Techniques               [36]   M. di Biase, A. Rastogi, M. Bruntink, and A. van Deursen. “The Delta
       in Static Code Analysis to Detect Weaknesses and Vulnerabilities.”                    Maintainability Model: Measuring Maintainability of Fine-Grained
       In: Canadian Conf. Artificial Intelligence. Vol. 8436. 2014, pp. 326–332.             Code Changes.” In: Int’l Conf. Technical Debt. IEEE, 2019, pp. 113–122.
[17]   Y. Zheng, S. Pujar, B. Lewis, L. Buratti, E. Epstein, B. Yang, J. Laredo, A.   [37]   R.-M. Karampatsis and C. Sutton. “How Often Do Single-Statement
       Morari, and Z. Su. “D2A: A Dataset Built for AI-Based Vulnerability                   Bugs Occur? The ManySStuBs4J Dataset.” In: Int’l Conf. Mining Softw.
       Detection Methods Using Differential Analysis.” In: Int’l Conf. Softw.                Repositories. 2020, pp. 573–577.
       Eng.: Softw. Eng. in Practice. IEEE, 2021, pp. 111–120.                        [38]   X. Li, L. Wang, Y. Xin, Y. Yang, and Y. Chen. “Automated Vulnerability
[18]   D. Mitropoulos, G. Gousios, P. Papadopoulos, V. Karakoidas, P. Louri-                 Detection in Source Code Using Minimum Intermediate Representa-
       das, and D. Spinellis. “The Vulnerability Dataset of a Large Software                 tion Learning.” In: Applied Sciences 10.5 (2020).
       Ecosystem.” In: Int’l Ws. Building Analysis Datasets and Gathering             [39]   N. Saccente, J. Dehlinger, L. Deng, S. Chakraborty, and Y. Xiong.
       Experience Returns for Security. IEEE, 2014, pp. 69–74.                               “Project Achilles: A Prototype Tool for Static Method-Level Vulner-
[19]   FindBugs. url: http://findbugs.sourceforge.net/ (visited on Jan. 25,                  ability Detection of Java Source Code Using a Recurrent Neural
       2021).                                                                                Network.” In: Int’l Conf. Autom. Softw. Eng. IEEE, 2019, pp. 114–121.
[20]   R. Raducu, G. Esteban, F. J. Rodríguez Lera, and C. Fernández. “Col-           [40]   H. K. Dam, T. Tran, T. T. M. Pham, S. W. Ng, J. Grundy, and A. Ghose.
       lecting Vulnerable Source Code from Open-Source Repositories for                      “Automatic Feature Learning for Predicting Vulnerable Software
       Dataset Generation.” In: Applied Sciences 10.4 (2020), p. 1270.                       Components.” In: IEEE Trans. Softw. Eng. 47.1 (2018), pp. 67–85.
[21]   Y. Zhou, S. Liu, J. Siow, X. Du, and Y. Liu. “Devign: Effective Vulnera-       [41]   P. Hegedűs. “Inspecting JavaScript Vulnerability Mitigation Patches
       bility Identification by Learning Comprehensive Program Semantics                     with Automated Fix Generation in Mind.” In: Int’l Conf. Computa-
       via Graph Neural Networks.” In: Conf. Neural Information Processing                   tional Science and Its Applic. Vol. 12252 LNCS. 2020, pp. 975–988.
       Systems. 2018, p. 11.                                                          [42]   M. Yang, J. Wu, S. Ji, T. Luo, and Y. Wu. “Pre-Patch: Find Hidden
[22]   Z. Li, D. Zou, S. Xu, X. Ou, H. Jin, S. Wang, Z. Deng, and Y. Zhong.                  Threats in Open Software Based on Machine Learning Method.” In:
       “VulDeePecker: A Deep Learning-Based System for Vulnerability                         World Congress on Services. Vol. 10975. 2018, pp. 48–65.
       Detection.” In: Network and Distributed System Security Symp. 2018.            [43]   A. Sabetta and M. Bezzi. “A Practical Approach to the Automatic
[23]   R. Vieira, A. da Silva, L. Rocha, and J. P. Gomes. “From Reports to                   Classification of Security-Relevant Commits.” In: Int’l Conf. Softw.
       Bug-Fix Commits: A 10 Years Dataset of Bug-Fixing Activity from                       Maintenance and Evolution. IEEE, 2018.
       55 Apache’s Open Source Projects.” In: Int’l Conf. Predictive Models           [44]   A. Larmuseau and D. Shila. “PatchSweetner: Exploit Detection Through
       and Data Analytics in Softw. Eng. ACM, 2019, pp. 80–89.                               the Automatic Transformation of Security Patches.” In: Military Com-
[24]   H. Alves, B. Fonseca, and N. Antunes. “Software Metrics and Secu-                     munications Conf. 2018, pp. 939–945.
       rity Vulnerabilities: Dataset and Exploratory Study.” In: European             [45]   Z. Chen, S. J. Kommrusch, M. Tufano, L.-N. Pouchet, D. Poshyvanyk,
       Dependable Computing Conf. 2016, pp. 37–44.                                           and M. Monperrus. “SEQUENCER: Sequence-to-Sequence Learning
[25]   A. Gkortzis, D. Mitropoulos, and D. Spinellis. “VulinOSS: A Dataset                   for End-to-End Program Repair.” In: IEEE Trans. Softw. Eng. (2019).
       of Security Vulnerabilities in Open-Source Systems.” In: Int’l Conf.           [46]   Z. Chen, S. Kommrusch, and M. Monperrus. Using Sequence-to-
       Mining Softw. Repositories. ACM, 2018, pp. 18–21.                                     Sequence Learning for Repairing C Vulnerabilities. arXiv: 1912.02015.
[26]   M. Jimenez, Y. Le Traon, and M. Papadakis. “Enabling the Continuous                   CoRR e-print, 2019.
       Analysis of Security Vulnerabilities with VulData7.” In: Int’l Working         [47]   E. Mashhadi and H. Hemmati. “Applying CodeBERT for Automated
       Conf. Source Code Analysis and Manipulation. 2018, pp. 56–61.                         Program Repair of Java Simple Bugs.” In: Int’l Conf. Mining Softw.
[27]   S. E. Ponta, H. Plate, A. Sabetta, M. Bezzi, and C. Dangremont. “A                    Repositories. IEEE, 2021, p. 5.
       Manually-Curated Dataset of Fixes to Vulnerabilities of Open-Source            [48]   B. Mosolygó, N. Vándor, G. Antal, and P. Hegedűs. “On the Rise and
       Software.” In: Int’l Conf. Mining Softw. Repositories. 2019, pp. 383–387.             Fall of Simple Stupid Bugs: A Life-Cycle Analysis of SStuBs.” In: Int’l
[28]   J. Fan, L. Li, S. Wang, and T. N. Nguyen. “A C/C++ Code Vulnerability                 Conf. Mining Softw. Repositories. IEEE, 2021, p. 5.
       Dataset with Code Changes and CVE Summaries.” In: Int’l Conf.                  [49]   F. Madeiral and T. Durieux. “A Large-Scale Study on Human-Cloned
       Mining Softw. Repositories. 2020, p. 5.                                               Changes for Automated Program Repair.” In: Int’l Conf. Mining Softw.
[29]   G. Lin, W. Xiao, J. Zhang, and Y. Xiang. “Deep Learning-Based Vul-                    Repositories. IEEE, 2021, p. 5.
       nerable Function Detection: A Benchmark.” In: Int’l Conf. Information          [50]   J. Hua and H. Wang. “On the Effectiveness of Deep Vulnerability
       and Communications Security. Vol. 11999. 2020, pp. 219–232.                           Detectors to Simple Stupid Bug Detection.” In: Int’l Conf. Mining
[30]   Y. Ma, T. Dey, C. Bogart, S. Amreen, M. Valiev, A. Tutko, D. Kennard,                 Softw. Repositories. IEEE, 2021, p. 5.
       R. Zaretzki, and A. Mockus. “World of Code: Enabling a Research                [51]   K. Herzig, S. Just, and A. Zeller. “The Impact of Tangled Code Changes
       Workflow for Mining and Analyzing the Universe of Open Source                         on Defect Prediction Models.” In: Empirical Softw. Eng. 21.2 (2016),
       VCS Data.” In: Empirical Softw. Eng. 26.2 (2021), p. 22.                              pp. 303–336.

## Strona 11

