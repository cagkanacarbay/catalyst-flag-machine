from app.pdf_utils import read_pdf
from app.openai import ask_jesus
from scripts.pickle_proposals import analyze_proposal_prompt_v1

# Test the function
pdf_text = read_pdf('proposals/Ideas-2023-07-13-12-37-43.pdf')





x = pdf_text.split("SDG rating")


result = ask_jesus(analyze_proposal_prompt_v1(y))

y = """
SDG goals:
Ensure inclusive and equitable quality education and promote lifelong learning
opportunities for all
Build resilient infrastructure, promote inclusive and sustainable industrialization
and foster innovation
SDG subgoals:
Significantly increase access to information and communications technology
and strive to provide universal and affordable access to the Internet in l ast
developed countries by 2030
How you perceive the problem you are solving
The lack of comprehensive online tooling and educational resources for
developers transitioning to Cardano. Currently, developers who want to
transition from other blockchain platforms to Cardano face challenges in finding
specific guidance and resources tailored to Cardano's ecosystem. This
knowledge gap impedes the growth and adoption of Cardano by limiting the
number of skilled developers who can effectively build and contribute to the
platform.
Your reasons for approaching it in the way that you have
We approach this problem by creating the Ethereum2Cardano University, an
innovative online portal and webinar platform. Our approach combines
educational assets with AI tools to provide developers with a comprehensive
and personalized learning experience. We believe that a combination of
structured educational materials, interactive webinars, and AI-powered tools
will address the specific needs of developers transitioning to Cardano, enabling
them to overcome the challenges they face during the migration process.
Who your project will engage
Our project will engage developers and community members who are
interested in transitioning to Cardano. We aim to cater to developers with
varying levels of experience, from beginners to experienced blockchain
developers. Additionally, we will actively involve the Cardano community by
Custom Fields:
encouraging participation in webinars, Q&A sessions, and knowledge-sharing
forums. By fostering collaboration and engagement, we aim to build a
supportive and vibrant community of developers within the Cardano
ecosystem.
How you will demonstrate or prove your impact
To demonstrate and prove our impact, we will employ various strategies.
Firstly, we will gather user feedback and evaluate engagement metrics to
assess the effectiveness and usefulness of the educational assets and AI tools
provided by the Ethereum2Cardano University. Additionally, we will track the
number of developers who successfully transition to Cardano and showcase
the projects and applications they build on the platform. The growth in the
number and quality of applications on Cardano will serve as a tangible
demonstration of the impact of our project in expanding the developer
community and fostering innovation within the Cardano ecosystem.
Answer:
The Ethereum2Cardano University directly addresses the challenge by
providing a comprehensive support system for developers and community
members transitioning to Cardano.
Specifics can be read below:
Creation and Improvement of Tools and Software
The online portal will offer a range of tools and software specifically designed
to make development on Cardano easier. These tools could include integrated
development environments (IDEs) tailored for Cardano smart contract
development, testing frameworks, deployment utilities, and libraries for
common functionalities. By providing these tools, Ethereum2Cardano
University empowers developers to build on Cardano more efficiently, reducing
the learning curve and increasing productivity. This in turn attracts more
developers to the ecosystem, leading to a broader range of on-chain
applications and innovations.
Support for SPO's (Stake Pool Operators)
The online portal will also offer resources and tools to help community
members operate stake pool nodes on the Cardano network. This includes
documentation, tutorials, and best practices for setting up and maintaining
stake pools, as well as monitoring and management tools. By simplifying the
process of running stake pools, Ethereum2Cardano University encourages
community members to actively participate in the network's decentralized
governance and security. This increased participation strengthens the Cardano
ecosystem by promoting decentralization and network resilience.
Research & Standards
The online portal will feature research papers, analysis reports and standards
documentation related to Cardano. These resources will contribute to the
broader understanding of the ecosystem and facilitate innovation. By
conducting research and fostering standards the Ethereum2Cardano
University helps advance the development of Cardano, promotes
interoperability and encourages collaboration among developers and
researchers.
Answer:
Developer Activity and Contributions
Tracking the number and quality of projects developed on Cardano by users of
the platform can serve as an indicator of success. Increased developer activity
and contributions demonstrate that the tools and resources provided are
enabling the creation of innovative apps on Cardano.
Adoption and Usage
The number of developers and community members using the online portal
and engaging with the AI tools can be a measure of success. Increased
adoption indicates that the platform is providing value and effectively
addressing the needs of the Cardano community.
Feedback
Collecting feedback from users about their experience with the tools,
resources, and webinars can provide insights into the platform's effectiveness.
Regular surveys, user ratings, and testimonials can be used to gauge user
satisfaction and identify areas for improvement.
Answer:
Collaboration with Cardano Foundation
Partnering with the Cardano Foundation to disseminate the outputs and results
of the project through their official channels. This collaboration can amplify the
reach and visibility of the University's initiatives and ensure widespread access
to the resources created.
Documentation and Reports
Publishing comprehensive documentation on the online portal that covers the
tools, standards, research, and analysis conducted by the University. These
documents can be openly accessible to the community and serve as a
valuable resource for developers and researchers.
Webinars and Workshops
Organizing regular webinars and workshops through the platform to share
insights, best practices, and updates on the latest developments in the
Cardano ecosystem. These interactive sessions can facilitate knowledge
sharing and foster a sense of community among developers and stakeholders.
Open-Source Contributions
We shall release relevant tools, libraries or frameworks as open-source
software where possibile. This allows the broader community to benefit from
the University's work and encourages collaboration and contributions from
other developers. Platforms like GitHub can be utilized for hosting and
maintaining open-source projects.
Answer:
Previously funded in F9 (eth2ada.com - Phase 1, Ethereum2Cardano
Dictionary) and closed out this proposal successfully.
We have already successfully deployed a staking app on Cardano mainnet that
supports staking for the following assets: NFTs, Liquidity Pool Tokens (from
any DEX; minswap, sundeaswap, musileswap, etc) and Native tokens:
Mainnet:
https://app.tangent.art
Preprod Testnet:
https://testnet.tangent.art
This app is popular and currently has over 200,000ADA total value locked
(TVL) and 100s of users who are very satisfied with the project.
Our capability to maintain these standards is grounded in our experience as a
team, full time 9 strong, transparent communication - be it in Town Hall
breakouts of elsewhere, community engagement - 5k + active community,
adherence to timelines and commitment to continuous improvement. We want
to stress that we are a full time team with commitments to build on Cardano.
Answer:
The Cardano2Ethereum University has 3 essential goals:
Facilitate ease of development on Cardano through the provision of
customized tools, research papers, databases, online portals, AI tooling and
software specifically tailored to meet both the needs of developers and the
community. User feedback, adoption rates of the tools, and their impact on
developer productivity will serve as indicators to validate the feasibility of this
goal.
Enhance education and empower stakeholders by creating educational
resources, documentation, and platforms for webinars and workshops.
Foster innovation and collaboration within the Cardano ecosystem is the third
primary goal of the project. This will be accomplished through research,
analysis, and the establishment of standards. The feasibility of this goal will be
measured by the quality and impact of the research outputs, adoption of the
standards by the community, and the level of collaboration achieved among
developers and researchers.
To validate the feasibility of our approach we will take the following steps.
Actively seek user feedback from developers, stakeholders and community
members through surveys, interviews, and user testing sessions. Positive
feedback, suggestions for improvement, and increased user engagement will
indicate the feasibility and effectiveness of our approach.
Monitor adoption rates and usage metrics, such as the number of active users,
frequency of usage and popularity of specific features available on the
University. Higher adoption rates will signify that our project is meeting the
needs of developers and community members
Assessing developer productivity and outcomes, including metrics like
development time, successful projects built on Cardano, and level of
innovation, will provide insights into the feasibility of our tools and support.
Lastly, we will measure the impact of our research and standards initiatives
through metrics like citations, collaborations, and contributions to the Cardano
knowledge base. By diligently evaluating these aspects, we will gather
meaningful data to validate the feasibility of our approach, allowing us to make
necessary adjustments and improvements to effectively serve the Cardano
ecosystem.
Answer:
1) Milestone: Online Portal Development
Design and development of the online portal architecture
Creation of user interface and user experience (UI/UX) design
Implementation of features and functionalities for tools, resources, and
documentation
Expected Timeline: 2 months
2) Milestone: AI Tools Integration
Research and selection of AI tools suitable for supporting users
Integration of AI tools into the online portal
Testing and refinement of AI tools for optimal performance
Expected Timeline: 1 month
3) Milestone: Webinar Platform Setup
Selection of appropriate webinar platform software or service
Customization of the webinar platform to align with project requirements
Integration of webinar platform with the online portal
Expected Timeline: 1 month
4) Milestone: Development Toolkits and Libraries
Identification of common functionalities required by developers on Cardano
Development of toolkits and libraries to streamline development processes
Documentation and examples for usage and integration
Expected Timeline: 3 months
5) Milestone: Stake Pool Operator Support
Custom Fields:
Creation of comprehensive documentation for setting up and maintaining stake
pools
Development of monitoring and management tools for stake pool operators
Integration of stake pool support features into the online portal
Expected Timeline: 2 months
6) Milestone: Research and Standards
Conduct research on Cardano ecosystem innovation and improvement areas
Analysis of existing standards and identification of gaps
Collaboration with stakeholders and researchers to develop new standards
and resources
Expected Timeline: 4 months
7) Milestone: Webinars and Workshops
Tasks:Planning and organization of educational webinars and workshops
Creation of educational resources and materials
Promotion and registration management for webinars and workshops
Expected Timeline: Ongoing, with periodic events throughout the project
duration
Expected Delivery Time = 12 Months
Answer:
Milestone 1: Online Portal Development
Deliverables: Fully functional online portal with an intuitive user interface and
user experience.
Outputs: Architecture design, UI/UX design, integrated features for tools /
Custom Fields:
resources / documentation.
Intended Outcome: Availability of a user-friendly online platform that serves as
a central hub for developers and stakeholders to access tools, resources and
documentation related to Cardano development and infrastructure.
Milestone 2: AI Tools Integration
Deliverables: Integration of AI tools into the online portal.
Outputs: Functioning AI tools integrated within the platform.
Intended Outcome: Availability of AI-powered tools that enhance the
development experience by providing intelligent assistance, automation and
analysis capabilities to developers and community members.
Milestone 3: Webinar Platform Setup
Deliverables: Configured and customized webinar platform integrated with the
online portal.
Outputs: Fully functional webinar platform with registration, hosting and
interactive features.
Intended Outcome: Capability to organize and host educational webinars,
workshops, and interactive sessions to facilitate knowledge sharing and
community engagement.
Milestone 4: Development Toolkits and Libraries
Deliverables: Development toolkits and libraries
Outputs: Well-documented toolkits and libraries that streamline development
processes and provide common functionalities.
Intended Outcome: Enhanced productivity and efficiency for developers on
Cardano, enabling them to build applications more effectively and reducing the
learning curve.
Custom Fields:
Milestone 5: Stake Pool Operator Support
Deliverables: Comprehensive stake pool documentation, monitoring and
management tools.
Outputs: Documentation, tutorials and tools to support stake pool operators in
setting up and managing their pools.
Intended Outcome: Increased participation of community members as stake
pool operators, leading to a more decentralized and secure Cardano network.
Milestone 6: Research and Standards
Deliverables: Research papers, analysis reports and standards documentation.
Outputs: Publications, reports and established standards for Cardano
development and infrastructure.
Intended Outcome: Advancement of the Cardano ecosystem through
innovation, collaboration and the establishment of best practices and
standards.
Milestone 7: Webinars and Workshops
Deliverables: Educational webinars, workshop materials, and resources.
Outputs: Recorded webinars, presentation materials and educational content.
Intended Outcome: Enhanced education and knowledge sharing within the
Cardano community, empowering stakeholders with the necessary skills and
understanding to actively contribute to the ecosystem.
Answer:
Online Portal Development - 50,000 ADA
UI/UX design and development: 30,000 ADA
Backend development and integration: 20,000 ADA
Custom Fields:
AI Tools Integration - 30,000 ADA
Research and selection of AI tools: 10,000 ADA
Integration and customization: 20,000 ADA
Webinar Platform Setup - 20,000 ADA
Webinar platform software or service: 10,000 ADA
Customization and integration: 10,000 ADA
Development Toolkits and Libraries - 40,000 ADA
Development of toolkits and libraries: 30,000 ADA
Documentation and examples: 10,000 ADA
Stake Pool Operator Support - 30,000 ADA
Stake pool documentation creation: 15,000 ADA
Monitoring and management tools development: 15,000 ADA
Research and Standards - 54,000 ADA
Research efforts: 40,000 ADA
Standards documentation and resources: 14,000 ADA
Webinars and Workshops - 20,000 ADA
Webinar organization and promotion: 10,000 ADA
Workshop materials and resources: 10,000 ADA
Miscellaneous and Contingency - 10,000 ADA
Reserved for unexpected expenses and contingencies
Total Budget: 224,000 ADA
Answer:
Clint Alexander // Chief Technology Officer
https://www.linkedin.com/in/clint-alexander-049742233/
calexander@tangent.art
Responsibilities within Tangent: overview / decision making / development /
basic coding
Bio:
Serial entrepreneur &amp; cryptocurrency enthusiast since 2013
Miner
Investor
Digital asset fund manager
Solidity back end smart contract development
CEO &amp; manufacturer of Bitcoin SHA256 ASIC miners and other electronic
hardware
Worked alongside Bitcoin mining hardware companies such as Bitmain,
Rockminer and Gekkoscience
----
Ben Gordon // Creative Director
https://www.linkedin.com/in/ben-gordon-352b37232/
bgordon@tangent.art
Responsibilities within Tangent: overview / decision making / marketing /
development
Bio:
Cryptocurrency enthusiast since 2017
Previous freelance marketing executive for a number of leading international
educational establishments in Asia
Previous retail company owner
Transitioned to blockchain project development in 2017
A knowledge of all stages from brand creation, overall strategy, research,
analysis, law and token creation.
Freelanced on a number of blockchain projects including Northern Lights
before creating Tangent in 2021
----
Marjan Zadeh// Senior Software Engineer&nbsp;
https://www.linkedin.com/in/marjankhodadadzadeh/
marjan@tangent.art
Responsibilities within Tangent: full stack / front end / back end
----
Benjamin Grabow // Software Engineer&nbsp;
https://www.linkedin.com/in/benjamin-grabow/

bgrabow@tangent.art
Responsibilities within Tangent: front-end development / coding
Answer:
The cost of the project provides value for money for the Cardano ecosystem in
several ways.
Firstly, the project aims to offer extensive support to developers and
stakeholders transitioning to Cardano. By investing in the development of an
online portal, AI tools, and educational initiatives the project ensures that the
ecosystem has the necessary support infrastructure in place once the industry
sees mass adoption. This comprehensive support enhances the overall
experience for developers, making it easier for them to build on Cardano and
increasing their productivity.
Secondly, the project focuses on providing resources, documentation and tools
specifically tailored to Cardano development. This targeted approach saves
developers time and effort by providing them with the necessary resources and
libraries they need to build applications on the platform.
Lastly, by fostering innovation, collaboration, and the establishment of
standards, the project contributes to the growth and advancement of the
Cardano ecosystem. This creates a more robust and vibrant ecosystem that
attracts more developers, stakeholders, and investors, ultimately increasing the
value and potential of the Cardano network.
Overall, the cost of the project represents a worthwhile investment as it brings
tangible benefits to the Cardano ecosystem, facilitates development, and helps
drive the ecosystem's long-term success.
"""