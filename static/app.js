/***Here all the input are taken by the id reference that by using method getElementByid ,
 * so do not change any ID in html */


const form = document.getElementById("chat-form");
const input = document.getElementById("chat-input");
const messages = document.getElementById("chat-messages");
const apiKey = "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";
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = input.value;
  input.value = "";

  messages.innerHTML += `<div class="message user-message">
   <span>${message}</span>
  </div>`;
//<img src="./icons/user.png" alt="user icon">
  // Use axios library to make a POST request to the OpenAI API
  const response = await axios.post(
    "https://api.openai.com/v1/completions",
    {
      prompt:"Explain the following code:\n "+message,
      model: "text-davinci-003",
      temperature: 0,
      max_tokens: 1000,
      top_p: 1,
      frequency_penalty: 0.0,
      presence_penalty: 0.0,
    },
    {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${apiKey}`,
      },
    }
  );
  const chatbotResponse = response.data.choices[0].text;

  messages.innerHTML += `<div class="message bot-message">
<span>${chatbotResponse}</span>
  </div>`;
  //  <img src="./icons/chatbot.png" alt="bot icon"> 
});