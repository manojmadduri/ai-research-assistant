import { useEffect, useState } from "react";

export default function HeroHeader() {
  const [darkMode, setDarkMode] = useState(true);

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }, [darkMode]);

  return (
    <header className="text-center">
      <div className="flex justify-between items-center max-w-4xl mx-auto mb-4 px-4">
        <h1 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-pink-500 to-violet-500">
          🧠 AI Research Assistant
        </h1>
        <button
          onClick={() => setDarkMode(!darkMode)}
          className="bg-gray-700 text-white px-4 py-1 rounded hover:bg-gray-600"
        >
          {darkMode ? "☀️ Light" : "🌙 Dark"}
        </button>
      </div>
      <p className="text-gray-400 text-lg">
        Upload documents. Ask brilliant questions. Get intelligent answers.
      </p>
    </header>
  );
}
