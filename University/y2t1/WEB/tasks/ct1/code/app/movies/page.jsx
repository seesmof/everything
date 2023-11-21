"use client";
import Input from "@/components/Input";
import Link from "next/link";
import { useEffect, useState } from "react";

const Catalog = () => {
  const [genres, setGenres] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState("");

  const fetchMovieGenres = async () => {
    const res = await fetch(
      `https://api.themoviedb.org/3/genre/movie/list?language=en&api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    setGenres(data.genres);
  };

  useEffect(() => {
    Promise.all([fetchMovieGenres()]).then(() => {
      setIsLoading(false);
    });
  }, []);

  return (
    <>
      <div className="max-w-6xl mx-auto p-4">
        <div className="flex items-center justify-between mb-4">
          <Input
            type="text"
            placeholder="Category Search..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full"
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
