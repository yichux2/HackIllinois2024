"use client";
import "./Home.css";
import { useState } from "react";

export default function Home() {
  const [file, setFile] = useState<File>();

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    console.log('calling req');
    e.preventDefault();
    if (!file) return;

    try {
      const data = new FormData();
      data.set("file", file);
      console.log('sending');
      const res = await fetch("/api/upload", {
        method: "POST",
        body: data,
      });
      // handle the error
      if (!res.ok) throw new Error(await res.text());
    } catch (e: any) {
      // Handle errors here
      console.error(e);
    }
  };

  return (
    <main>
      <div className="banner">Chiba Math</div>
      <div className="grid">
        <div className="block1">
          Flex 1
          <form onSubmit={onSubmit}>
            <input
              type="file"
              name="file"
              onChange={(e) => setFile(e.target.files?.[0])}
            />
            <input type="submit" value="Upload" />
          </form>
        </div>
        <div className="block2">Flex 2</div>
      </div>
    </main>
  );
}
// }
