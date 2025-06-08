import { useState } from "react";
import axios from "axios";
import Spinner from "./Spinner";

export default function AnimatedUpload() {
  const [file, setFile] = useState(null);
  const [msg, setMsg] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const upload = async () => {
    setIsLoading(true);
    try {
      const formData = new FormData();
      formData.append("file", file);
      const res = await axios.post("http://localhost:8000/upload/", formData);
      setMsg(res.data.details);
    } catch (err) {
      setMsg("Upload failed.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="bg-white/5 backdrop-blur-sm p-6 rounded-xl border border-white/10 shadow-xl">
      <h2 className="text-2xl font-semibold mb-4">📄 Upload Document</h2>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-3 block w-full text-sm text-gray-300 bg-gray-800 rounded-lg px-3 py-2"
      />
      {isLoading ? (
        <Spinner />
      ) : (
        <button
          onClick={upload}
          className="bg-gradient-to-r from-green-500 to-emerald-600 hover:from-green-600 hover:to-emerald-700 text-white px-5 py-2 rounded transition shadow"
        >
          Upload
        </button>
      )}
      {msg && <p className="mt-3 text-green-400 text-sm">{msg}</p>}
    </div>
  );
}
