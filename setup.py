from setuptools import find_packages, setup

setup(
    name = "WebSage",
    version="0.0.1",
    description="""Introducing WebSage, an innovative Rag-based chatbot designed to
    revolutionize your web browsing experience. With WebSage, you can effortlessly 
    interact with any website by simply inputting its URL. Leveraging cutting-edge 
    FAISS vectorization technology, WebSage fetches and stores website content in 
    its vector store, enabling lightning-fast access to information. Whether you're 
    seeking specific details or exploring general topics, WebSage delivers tailored 
    results based on your queries, offering a seamless and intuitive browsing experience."
    """,
    long_description="""WebSage is an advanced Rag-based chatbot that redefines the way users 
    interact with websites. Powered by state-of-the-art FAISS vectorization technology, WebSage
    seamlessly integrates with any web page, allowing users to access and query website content
    directly through conversational interactions. By inputting a website's URL, users can unlock
    a treasure trove of information stored within WebSage's comprehensive vector store.
    At the heart of WebSage lies its sophisticated vectorization engine, which utilizes 
    FAISS (Facebook AI Similarity Search) to transform textual and visual content from websites 
    into high-dimensional vectors. These vectors are then indexed and stored within WebSage's vector
    store, enabling rapid and efficient retrieval of relevant information based on user queries.
    WebSage's intelligent chat interface empowers users to engage in natural language conversations,
    posing questions, seeking clarifications, or expressing interests about specific topics within the
    context of the website content. Whether it's extracting product details, browsing news articles,
    or exploring educational resources, WebSage intelligently interprets user queries and retrieves 
    accurate responses from its vast vector store.
    Moreover, WebSage's Rag (Retrieval-Augmented Generation) architecture enhances its conversational
    capabilities, allowing it to generate informative and contextually relevant responses 
    based on user interactions. By combining retrieval and generation techniques, WebSage delivers 
    personalized and engaging conversations tailored to each user's preferences and interests.
    WebSage's versatility extends beyond traditional web browsing, offering users a multifaceted
    experience that transcends conventional search engines. Whether you're a researcher, student,
    journalist, or curious explorer, WebSage empowers you to dive deep into the web's vast repository
    of knowledge, providing instant access to valuable insights and information.
    """,
    author="Ved Prakash Pathak",
    packages=find_packages(),
    
)