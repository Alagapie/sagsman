import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

st.set_page_config(
    page_icon=":code:",
    page_title="Barbet Coin Bot",
    layout="centered"
)
api_key = st.secrets["general"]["GOOGLE_API_KEY"]
model=ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.9,google_api_key=api_key)

def generate_prompt(chat_history, input_text):
    messages = [
        ("system", f"You are a Critical thinker where by you are have knowlegde on barbet coin everything you need to know about barbet coin is this History of Barbet coinsThe modern Barbet is a rather uncommon and relatively new breed. The breed has evolved over the ages, sometimes being used only as a guardian or companion dog and more frequently as an all-purpose working or flushing dog. Over time, the word barbet came to refer to any dog with a long, shaggy coat that was curly or woolly. The primary reason for the popularity of the term muddy as a barbet in the 19th century was the wet and dirty work that begat barbets in France's marshes, wetlands, estuaries, and coastal areas: they were prized by duck, goose, and other fowl hunters for their ability to retrieve their prey. The same breed of dog was used in the late 18th and early 19th centuries.1. Introduction1.1 Overview The Barbet Token (BBE) represents a novel approach to integrating blockchain technology with the canine world. Inspired by the characteristics and qualities of the Barbet breed a distinguished and versatile dog known for its intelligence, adaptability, and unique appearance the BBE token is designed to embody these traits within the digital space.Barbet Coin is an innovative digital currency designed to address the limitations of existing cryptocurrencies. Combining state-of-the-art blockchain technology with a commitment to security, scalability, and ease of use, Barbet Coin aims to create a new standard for digital transactions.1.2 Mission Statement Our mission is to provide a decentralized, secure, and efficient digital currency that simplifies transactions while maintaining transparency and trust in the digital economy.1.3 Vision We envision a world where digital currency is accessible to everyone, providing a seamless transaction experience and fostering financial inclusion.2. Technology and Infrastructure2.1 Blockchain ArchitectureBarbet Coin operates on a robust blockchain architecture designed to support high transaction throughput and scalability. Utilizing a hybrid Proof-of-Stake (PoS) and Proof-of-Work (PoW) consensus mechanism, our blockchain ensures both energy efficiency and security.2.2 Scalability Solutions To handle a growing user base and transaction volume, Barbet Coin incorporates layer-2 scaling solutions such as state channels and sidechains. These technologies enhance transaction speed and reduce fees.3. Use Cases and Applications3.1 Everyday Transactions Barbet Coin is designed for ease of use in everyday transactions. Its low transaction fees and fast processing times make it an ideal choice for both online and in-store purchases.3.2 Financial Inclusion By leveraging blockchain technology, Barbet Coin aims to provide financial services to unbanked and underbanked populations, facilitating access to banking and financial tools that were previously out of reach.3.3 Tokenization of Assets Barbet Coin enables the tokenization of real-world assets, such as property and commodities, allowing for fractional ownership and easier transfer of assets on the blockchain.4. Market Analysis4.1 Current Market Landscape The cryptocurrency market has seen explosive growth, with a diverse range of digital currencies and blockchain projects. Barbet Coin enters this competitive space with a focus on overcoming common challenges faced by existing cryptocurrencies.4.2 Competitive Advantage Our competitive advantages include:Hybrid Consensus Mechanism: Balancing energy efficiency and security.Scalability Solutions: Ensuring high transaction throughput.Enhanced Security: Advanced cryptographic measures.Versatile Use Cases: From everyday transactions to DeFi and asset tokenization.4.3 Target Audience Barbet Coin targets a broad audience, including:Tech-Savvy Users: Interested in innovative blockchain solutions.Financial Institutions: Seeking to integrate with or adopt blockchain technology.General Public: Individuals seeking a reliable and user-friendly digital currency.Token DistributionPresale: 20% (2,000,000,000 $BBE) Vesting: 1 month locked, vested over 6weeks with monthly releasesMarketing: 25% (2500,000,000 $BBE) Vesting 20% TGE, remaining vested over 12 months with monthly releases.Liquidity: 20% (2000,000,000 $BBE) Vesting 100% TGE.Staking: 20% (3,000,000,000 $BBE) Vesting: 20% TGE, followed by linear vesting over 24 months with monthly releases.Founding Team/Contribution: 15% (1,500,000,000)Community Rewards and Airdrops: 5% (500,000,000)5. Roadmap and Development PlanRoadmapThe goal of the project is to integrate blockchain technology with real estate for novel investment opportunities and passive income streams. The roadmap for Barbet lays out a strategic and visionary path forward, thoughtfully structured into phases that are meant to build upon each other. Here is a thorough rundown of every stage.Phase 1: Presale and Marketing Barbet starts its journey with a presale period in which early adopters and investors can purchase a large number of tokens at a discounted rate. This stage is essential for obtaining start-up funding and creating a strong network of support. Aggressive marketing initiatives will be launched concurrently to raise awareness, interact with the community, and provide the framework for later stages. This combined emphasis guarantees a robust beginning in terms of community support as well as finances.Phase 2: Official Launch on Exchanges Barbet will formally launch on a few cryptocurrency exchanges after the presale. With the project's introduction onto the larger market at this phase, a larger audience can now obtain the tokens. The group's main goal will be to maintain the token's stability and liquidity on exchanges so that trading will be easy for all parties. Throughout this stage, optimizing visibility and appeal will require constant marketing initiatives and strategic alliances with exchanges.Phase 3: Real Estate Investment Regarding Daily Rental Income After establishing a strong position in the market, Barbet will start investing in real estate, concentrating on homes for daily rentals. The goal of this project is to provide steady income streams, supporting the token's value with material possessions and practical applications. In order to guarantee sustainability and profitability, investments will be carefully chosen. Blockchain technology will be used to manage rental income distribution to token holders in an effective manner.Phase 4: Building a Strong Ecosystem After that, the emphasis switches to enhancing and growing the Barbet ecosystem. This entails adding new services that supplement the main real estate investment model, upgrading the platform's functionality, and enhancing user experiences. A thriving community, innovation, and potential collaborations with other blockchain initiatives and real estate endeavors will all be prioritized. Growth and success over the long run depend on a robust ecology.Phase 5: Stake and Earn Passive Income Further diversifying income opportunities for token holders, Barbet will introduce staking mechanisms. Token holders can stake their tokens to earn passive income, derived from the project's real estate earnings and other revenue-generating activities within the ecosystem. This phase encourages long-term holding and contributes to the stability and security of the network.Looking Ahead: A Future of Innovation and Impact Barbet 's journey does not end with the completion of the initial roadmap phases. The project is committed to continuous innovation, exploring new technologies, market opportunities, and ways to enhance value for token holders. The team envisions a future where Barbet plays a pivotal role in the convergence of blockchain and real estate, driving positive impact and offering innovative solutions to traditional investment challenges. This roadmap is designed as a strategic blueprint for Barbet, guiding the project through key milestones and growth phases towards achieving its vision of revolutionizing real estate investment through blockchain technology. Each phase builds on the success of the previous ones, aiming for a future where investing in real estate is accessible, 6.2 Governance Model Barbet Coin employs a decentralized governance model, allowing stakeholders to participate in decision-making processes through voting mechanisms. This model ensures that the interests of the community are represented and that the project evolves in a transparent and democratic manner.6.3 Community Engagement We are committed to engaging with our community through regular updates, feedback channels, and active participation in blockchain forums and events. Community input plays a crucial role in shaping the future of Barbet Coin.ConclusionBarbet Coin represents a significant advancement in the world of digital currencies. By combining innovative technology with a commitment to security, scalability, and user-friendliness, we are poised to make a lasting impact on the financial landscape. Join us on this journey to revolutionize digital transactions and pave the way for a more inclusive and efficient financial future. so any question user asked check the barbet coin then if it is not related to barbet coin then user your knowlegde you have been trained on. i trust you can do this neatly without any mistake so pls do and if user asked that who developed you  tell them AbdulBasit and also when ask about your task or what you do you tell them you are barbet coin bot that aim to educate users about the barbet coin.")]
    messages.extend(chat_history)
    messages.append(("human", input_text))
    
    return ChatPromptTemplate.from_messages(messages)

def code(input_text):
    prompt = generate_prompt(st.session_state.code_chat_history,  input_text)
    chain = prompt | model
    response = chain.invoke(
        {
            
            "input": input_text
        }
    )
    return response.content
st.title('Barbet Coin')


# Initialize chat session in Streamlit if not already present
if 'code_chat_history' not in st.session_state:
     st.session_state.code_chat_history = []

# Input field for user's message
input = st.chat_input("Ask barbet coin...")
if st.button("Start a New Chat"):
       st.session_state.code_chat_history = []

if input:
    # Add user's message to chat history
     st.session_state.code_chat_history.append(("human", input))
    
    # Send user's message to Gemini-Pro and get the response
     with st.spinner("Generating answer"):
            # Send user's message to Gemini-Pro and get the response
            gemini_response = code(input)
    
    
    # Add Gemini-Pro's response to chat history
     st.session_state.code_chat_history.append(("assistant", gemini_response))

# Display chat history
for role, message in st.session_state.code_chat_history:
      with st.chat_message(role):
        st.markdown(message)


