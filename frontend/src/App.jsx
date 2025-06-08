import HeroHeader from "./components/HeroHeader";
import AnimatedUpload from "./components/AnimatedUpload";
import ChatWindow from "./components/ChatWindow";
import AgentSelector from "./components/AgentSelector";
import ScrollToTop from "./components/ScrollToTop";

function App() {
  return (
    <div className="min-h-screen flex flex-col items-center px-4 pt-10">
      <HeroHeader />
      <div className="mt-10 w-full max-w-7xl grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="space-y-6">
          <AgentSelector />
          <AnimatedUpload />
          <ScrollToTop />
        </div>
        <ChatWindow />
      </div>
    </div>
  );
}

export default App;
