import { useState } from "react";
import axios from "axios";

export default function ChatWindow() {
  const [query, setQuery] = useState("");
  const [chat, setChat] = useState([]);

  const handleSend = async () => {
    if (!query.trim()) return;
    const userMsg = { sender: "user", text: query };
    setChat([...chat, userMsg]);
    setQuery("");
    const res = await axios.post("http://localhost:8000/query/", { query });
    const aiMsg = { sender: "ai", text: res.data.response };
    setChat((prev) => [...prev, aiMsg]);
  };

  return (
    <div className="bg-gray-800 p-6 rounded-xl shadow-lg h-full flex flex-col">
      <h2 className="text-xl font-semibold mb-4">💬 Chat</h2>
      <div className="flex-1 overflow-y-auto bg-gray-900 rounded p-3 space-y-2 mb-4">
        {chat.map((msg, i) => (
          <div
            key={i}
            className={`text-sm flex ${
              msg.sender === "user" ? "justify-end" : "justify-start"
            }`}
          >
            <span className={`px-3 py-2 rounded-lg max-w-xs ${
              msg.sender === "user"
                ? "bg-blue-600 text-white"
                : "bg-gray-700 text-white"
            }`}>
              {msg.text}
            </span>
          </div>
        ))}
      </div>
      <div className="flex">
        <input
          className="flex-1 p-2 rounded-l-lg bg-gray-700 text-white"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask something..."
        />
        <button
          onClick={handleSend}
          className="bg-indigo-600 px-4 py-2 rounded-r-lg hover:bg-indigo-700 transition"
        >
          Send
        </button>
      </div>
    </div>
  );
}
