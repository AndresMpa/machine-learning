import { env } from "../util/env";
import { useState } from "react";
import "../style/App.css";

const App = () => {
  const [file, setFile] = useState();
  const [analysis, setAnalysis] = useState();

  const handleFileLoad = (event) => {
    event.preventDefault();
    if (event.target.files) {
      setFile(event.target.files[0]);
    }
  };

  const handleFileSubmit = () => {
    if (!file) {
      return "No file provided";
    }
    console.log(`${env.BASE_URL}/`);

    fetch(`${env.BASE_URL}/`, {
      method: "POST",
      body: file,
      headers: {
        "content-type": file.type,
        "content-length": `${file.size}`,
      },
    })
      .then((res) => res.json())
      .then((data) => setAnalysis(data))
      .catch((error) => console.error(error));
  };

  return (
    <div className="App">
      <header>
        <h1>Simple test app</h1>
      </header>
      <main className="App-header">
        <section>
          <form onSubmit={handleFileLoad}>
            <input type="file" name="file" onChange={handleFileLoad} />
            <button type="submit" onClick={handleFileSubmit}>
              Send
            </button>
          </form>
        </section>
        {analysis && (
          <section>
            <article>
              <h2>File</h2>
            </article>
          </section>
        )}
      </main>
    </div>
  );
};

export default App;
