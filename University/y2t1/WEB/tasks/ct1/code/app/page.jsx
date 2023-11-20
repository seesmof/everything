"use client";
import PosterCard from "@/components/home/PosterCard";
import PosterCardSkeleton from "@/components/home/PosterCardSkeleton";
import Link from "next/link";
import { useEffect, useState } from "react";

export default function Home() {
  const [trendingMovies, setTrendingMovies] = useState([]);
  const [popularMovies, setPopularMovies] = useState([]);
  const [topRatedMovies, setTopRatedMovies] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const fetchTrendingMovies = async () => {
    const res = await fetch(
      `https://api.themoviedb.org/3/movie/now_playing?api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    let filteredData = data.results.filter(
      (result) => result.original_language !== "ru"
    );
    filteredData = filteredData.slice(0, 8);
    console.log(filteredData);
    setTrendingMovies(filteredData);
  };

  const fetchPopularMovies = async () => {
    const res = await fetch(
      `https://api.themoviedb.org/3/movie/popular?api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    let filteredData = data.results.filter(
      (result) => result.original_language !== "ru"
    );
    filteredData = filteredData.slice(0, 8);
    console.log(filteredData);
    setPopularMovies(filteredData);
  };

  const fetchTopRatedMovies = async () => {
    const res = await fetch(
      `https://api.themoviedb.org/3/movie/top_rated?api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    let filteredData = data.results.filter(
      (result) => result.original_language !== "ru"
    );
    filteredData = filteredData.slice(0, 8);
    console.log(filteredData);
    setTopRatedMovies(filteredData);
  };

  useEffect(() => {
    Promise.all([
      fetchTrendingMovies(),
      fetchPopularMovies(),
      fetchTopRatedMovies(),
    ]).then(() => {
      setIsLoading(false);
    });
  }, []);

  return (
    <>
      <main className="grid p-4 gap-4 pb-16 max-w-6xl mx-auto">
        <section className="grid">
          <h2 className="font-bold pb-2 md:pb-4 md:pt-4 text-xl md:text-2xl text-slate-50">
            Popular Today
          </h2>
          {isLoading ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
              {Array.from({ length: 8 }).map((_, index) => (
                <PosterCardSkeleton key={index} />
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
              {trendingMovies.map((movie) => (
                <PosterCard
                  key={movie.id}
                  id={movie.id}
                  image={`https://image.tmdb.org/t/p/original${movie.poster_path}`}
                  name={movie.title}
                  release_year={movie.release_date.slice(0, 4)}
                  media_type="movie"
                />
              ))}
            </div>
          )}
          <div className="flex md:justify-end mt-2 mb-2">
            <Link
              href={"/movies"}
              className="bg-slate-800 text-slate-300 p-2 px-4 w-full md:w-max text-center rounded-md duration-300 hover:bg-slate-700"
            >
              View All
            </Link>
          </div>
        </section>
        <section className="grid">
          <h2 className="font-bold pb-2 md:pb-4 md:pt-4 text-xl md:text-2xl text-slate-50">
            Trending
          </h2>
          {isLoading ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
              {Array.from({ length: 8 }).map((_, index) => (
                <PosterCardSkeleton key={index} />
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
              {popularMovies.map((movie) => (
                <PosterCard
                  key={movie.id}
                  id={movie.id}
                  image={`https://image.tmdb.org/t/p/original${movie.poster_path}`}
                  name={movie.title}
                  release_year={movie.release_date.slice(0, 4)}
                  media_type="movie"
                />
              ))}
            </div>
          )}
          <div className="flex md:justify-end mt-2 mb-2">
            <Link
              href={"/movies"}
              className="bg-slate-800 text-slate-300 p-2 px-4 w-full md:w-max text-center rounded-md duration-300 hover:bg-slate-700"
            >
              View All
            </Link>
          </div>
        </section>
        <section className="grid">
          <h2 className="font-bold pb-2 md:pb-4 md:pt-4 text-xl md:text-2xl text-slate-50">
            Top Rated
          </h2>
          {isLoading ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
              {Array.from({ length: 8 }).map((_, index) => (
                <PosterCardSkeleton key={index} />
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
              {topRatedMovies.map((movie) => (
                <PosterCard
                  key={movie.id}
                  id={movie.id}
                  image={`https://image.tmdb.org/t/p/original${movie.poster_path}`}
                  name={movie.title}
                  release_year={movie.release_date.slice(0, 4)}
                  media_type="movie"
                />
              ))}
            </div>
          )}
          <div className="flex md:justify-end mt-2 mb-2">
            <Link
              href={"/movies"}
              className="bg-slate-800 text-slate-300 p-2 px-4 w-full md:w-max text-center rounded-md duration-300 hover:bg-slate-700"
            >
              View All
            </Link>
          </div>
        </section>
      </main>
    </>
  );
}
