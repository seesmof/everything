"use client";
import Link from "next/link";
import { useState } from "react";

const About = () => {
  const [nameInput, setNameInput] = useState("");
  const [emailInput, setEmailInput] = useState("");
  const [messageInput, setMessageInput] = useState("");

  const clearInputs = () => {
    setNameInput("");
    setEmailInput("");
    setMessageInput("");
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Name:", nameInput);
    console.log("Email:", emailInput);
    console.log("Message:", messageInput);
    clearInputs();
  };

  return (
    <>
      <div className="max-w-6xl mx-auto p-4 grid text-neutral-200 pb-20">
        <img
          src="https://blog.richersounds.com/wp-content/uploads/2016/02/matrix-reloaded-fight-scene-radically-recut-with-8-bit-sound1.png"
          alt="General Page Image - A scene from Interstellar"
          className="rounded-xl w-full object-cover"
        />
        <div className="grid space-y-3 md:space-y-4">
          <h1 className="text-3xl font-bold mt-4 md:mt-6">About Flickster</h1>
          <p>
            Flickster is a web application designed to provide an intuitive and
            user-friendly platform for browsing and selecting movies. With a
            vast database of movies, Flickster offers detailed information about
            each movie, including a full description, similar movies, and user
            ratings.
          </p>
          <h2 className="font-bold text-xl pt-2">
            The Motivation Behind Flickster
          </h2>
          <p>
            The idea behind Flickster was born out of a passion for movies and a
            desire to simplify the process of browsing and selecting movies.
            With the rise of streaming services and online movie databases,
            there's more content available than ever before. However, navigating
            these platforms can be overwhelming, with endless options and a lack
            of structure.
          </p>
          <p>
            Flickster aims to address this issue by providing a simple, clean
            interface that makes it easy to browse and select movies. Whether
            you're looking for a movie to watch tonight, or you're on the hunt
            for your next favorite series, Flickster is the place to go.
          </p>
          <blockquote className="border-l-4 border-indigo-500 pl-4 italic">
            "A film is like a novel, but instead of being written, it's filmed."
          </blockquote>
          <h2 className="font-bold text-xl pt-2">The History of Movies</h2>
          <p>
            Movies have been a staple of popular culture since the early 20th
            century. From the silent films of the 1920s to the blockbuster
            action movies of today, movies have evolved to reflect the times.
            They've captured our imaginations, sparked debates, and shaped our
            understanding of the world.
          </p>
          <h2 className="font-bold text-xl pt-2">Why Movies Matter</h2>
          <p>
            Movies are more than just entertainment. They're a reflection of our
            culture, our society, and our times. They tell stories, they make us
            laugh, they make us cry, and they inspire us. They're a universal
            language that transcends borders and cultures.
          </p>
          <h2 className="font-bold text-xl pt-2">Why Flickster is Useful</h2>
          <p>
            Flickster is a tool that makes browsing and selecting movies easier
            and more enjoyable. With its simple interface and comprehensive
            database, Flickster allows you to find the perfect movie for any
            occasion. Whether you're looking for a movie to watch with friends,
            or you're on the hunt for your next favorite series, Flickster is
            here to help.
          </p>
          <h2 className="font-bold text-xl pt-2">Contact Information</h2>
          <p>
            For more information about Flickster, or if you have any questions
            or comments, feel free to contact us.
          </p>
          <div className="flex items-center gap-2">
            <Link
              className="underline underline-offset-2 decoration-2 decoration-indigo-500 hover:text-white hover:decoration-indigo-400 duration-300"
              href="https://github.com/seesmof"
            >
              GitHub
            </Link>
            <Link
              className="underline underline-offset-2 decoration-2 decoration-indigo-500 hover:text-white hover:decoration-indigo-400 duration-300"
              href="mailto:seesmwork@gmail.com"
            >
              Email
            </Link>
          </div>
          <h2 className="font-bold text-xl pt-2">Contact Us</h2>
          <p>
            Please fill out the form below if you have any questions left and
            we'll get back to you.
          </p>
          <div className="grid gap-4">
            <div className="grid gap-2">
              <label htmlFor="name" className="font-medium cursor-pointer">
                Name
              </label>
              <input
                type="text"
                id="name"
                className="rounded-xl p-2 px-3 bg-inherit border-2 border-neutral-700 hover:border-indigo-600 focus:outline-none focus:border-indigo-600"
                placeholder="Your name..."
                value={nameInput}
                onChange={(e) => setNameInput(e.target.value)}
              />
            </div>
            <div className="grid gap-2">
              <label htmlFor="email" className="font-medium cursor-pointer">
                Email
              </label>
              <input
                type="email"
                id="email"
                className="rounded-xl p-2 px-3 bg-inherit border-2 border-neutral-700 hover:border-indigo-600 focus:outline-none focus:border-indigo-600"
                placeholder="Your email..."
                value={emailInput}
                onChange={(e) => setEmailInput(e.target.value)}
              />
            </div>
            <div className="grid gap-2">
              <label htmlFor="message" className="font-medium cursor-pointer">
                Message
              </label>
              <input
                type="text"
                id="message"
                className="rounded-xl p-2 px-3 bg-inherit border-2 border-neutral-700 hover:border-indigo-600 focus:outline-none focus:border-indigo-600"
                placeholder="Your message..."
                value={messageInput}
                onChange={(e) => setMessageInput(e.target.value)}
              />
            </div>
            <button
              className="bg-indigo-600 hover:bg-indigo-500 duration-300 text-white font-medium rounded-xl p-2 px-4 md:px-6 w-full sm:w-max active:scale-95"
              type="submit"
              onClick={handleSubmit}
            >
              Submit
            </button>
          </div>
          <p className="text-slate-300 text-sm text-center hidden sm:block">
            Web technology and design @2023
          </p>
        </div>
      </div>
    </>
  );
};

export default About;
