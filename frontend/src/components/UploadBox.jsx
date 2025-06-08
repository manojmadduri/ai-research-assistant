import { useState } from "react";
import axios from "axios";

function UploadBox() {
  const [file, setFile] = useState(null);
  const [msg, setMsg] = useState("");

  const upload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios.post("http://localhost:8000/upload/", formData);
    setMsg(res.data.details);
  };

  return (
    <div className="bg-gray-800 p-4 rounded-lg w-full max-w-xl shadow">
      <h2 className="text-xl font-semibold mb-2">📄 Upload Document</h2>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-2 block w-full text-sm text-gray-300 bg-gray-900 rounded px-2 py-1"
      />
      <button
        onClick={upload}
        className="bg-green-600 px-4 py-2 rounded hover:bg-green-700 transition"
      >
        Upload
      </button>
      {msg && <p className="mt-2 text-green-400">{msg}</p>}
    </div>
  );
}

export default UploadBox;