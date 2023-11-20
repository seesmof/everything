"use client";
import Link from "next/link";
import { useEffect, useState } from "react";

const Catalog = () => {
  const [genres, setGenres] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState("");

  const fetchShowsGenres = async () => {
    const res = await fetch(
      `https://api.themoviedb.org/3/genre/tv/list?language=en&api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    setGenres(data.genres);
  };

  useEffect(() => {
    Promise.all([fetchShowsGenres()]).then(() => {
      setIsLoading(false);
    });
  }, []);

  return (
    <>
      <div className="max-w-6xl mx-auto p-4 grid">
        <div className="flex items-center justify-between mb-4">
          <input
            type="text"
            className="w-full bg-inherit border-2 border-neutral-700 rounded-xl p-2"
            placeholder="Category search..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
        </div>

        {isLoading ? (
          <div className="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-4">
            {Array.from({ length: 20 }).map((_, index) => (
              <div
                key={index}
                className="flex aspect-square items-center justify-center rounded-xl bg-neutral-700 animate-pulse"
              ></div>
            ))}
          </div>
        ) : (
          <div className="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-4">
            {genres
              .filter((genre) =>
                genre.name.toLowerCase().includes(searchQuery.toLowerCase())
              )
              .map((genre) => (
                <Link
                  key={genre.id}
                  href={`/catalog/${genre.id}`}
                  className="flex aspect-square items-center justify-center rounded-xl bg-neutral-700 duration-300 hover:bg-neutral-600"
                >
                  <p className="text-2xl">{genre.name}</p>
                </Link>
              ))}
          </div>
        )}
      </div>
    </>
  );
};

export default Catalog;
