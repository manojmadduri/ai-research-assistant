export default function AgentSelector() {
    return (
      <div className="w-full">
        <label className="block mb-1 text-sm font-medium text-gray-300">Agent Type</label>
        <select className="w-full bg-gray-800 text-white p-2 rounded-lg shadow">
          <option value="default">Default (OpenAI)</option>
          <option value="multi">Multi-Agent</option>
          <option value="lora">Fine-Tuned</option>
        </select>
      </div>
    );
  }
  