# 🤖 AI Chatbot with Token-by-Token Streaming

An advanced AI chatbot application built using **LangGraph**, enabling real-time, token-by-token responses for an interactive user experience. This project demonstrates the integration of **streaming APIs**, **stateful conversation management**, and **dynamic response generation**.

---

## 🚀 Project Overview

This AI chatbot utilizes LangGraph's streaming capabilities to provide real-time responses, enhancing user interaction by delivering tokens as they are generated. The system is designed to handle complex conversational flows, including intent recognition, dynamic response generation, and tool integration.

**Key Features:**
- **Real-Time Token Streaming:** Delivers responses token by token for an interactive experience.
- **Stateful Conversations:** Maintains context across interactions to provide coherent responses.
- **Dynamic Response Generation:** Utilizes advanced language models to generate contextually relevant replies.
- **Tool Integration:** Incorporates external tools and APIs to enrich the conversation.

---

## 🧠 Architecture

The chatbot is structured using LangGraph's node-based framework, where each node represents a specific function or action in the conversation flow. The core components include:

- **State Management:** Maintains conversation history and context.
- **Streaming Node:** Handles the real-time streaming of tokens.
- **Response Generation:** Utilizes language models to generate responses.
- **Tool Nodes:** Integrates external tools for additional functionalities.

---

## ⚙️ Setup & Installation

To run the AI chatbot locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mohdzaid72/LangGraph.git
   cd LangGraph/chatbot
   ```

2. **Install Dependencies:**
   Ensure you have Python 3.8+ installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**
   Create a `.env` file in the root directory and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_API_KEY=your_google_api_key
   ```

4. **Run the Application:**
   Start the chatbot application:
   ```bash
   python app.py
   ```

5. **Access the Chat Interface:**
   Open your browser and navigate to `http://localhost:5000` to interact with the chatbot.

---

## 🧪 Usage

Once the application is running, you can initiate a conversation by typing your message into the chat interface. The chatbot will process your input and respond in real-time, delivering tokens as they are generated.

**Example Interaction:**
- **User:** "What's the weather like today?"
- **Chatbot:** "Fetching the latest weather information..."

The chatbot will continue to provide updates as new tokens are generated, offering a dynamic and engaging conversation experience.

---

## 🔧 Technologies Used

- **LangGraph:** Framework for building and orchestrating AI agents.
- **OpenAI API:** Provides language model capabilities for response generation.
- **Google API:** Used for integrating external tools and services.
- **Python:** Programming language for backend development.
- **Flask:** Web framework for serving the chatbot application.

---
## 🧑‍💻 Author

**Mohd Zaid**  

📧 mohdzaidonly@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/mohd-zaid-5b6452233/) | 🔗 [GitHub](https://github.com/mohdzaid72)  
---

## 🚀 Future Enhancements

- **Multimodal Capabilities:** Integrate voice and image processing for a richer interaction.
- **Advanced Memory Management:** Implement long-term memory to remember user preferences across sessions.
- **Deployment:** Host the application on cloud platforms like AWS or Heroku for public access.
- **User Feedback Integration:** Allow users to provide feedback to improve chatbot responses.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

For any inquiries or contributions, please contact [mohdzaidonly@gmail.com](mailto:mohdzaidonly@gmail.com).

---

⭐ If you find this project interesting, consider giving it a star!
