"use client";
import PosterCard from "@/components/home/PosterCard";
import PosterCardSkeleton from "@/components/home/PosterCardSkeleton";
import Link from "next/link";
import { useEffect, useState } from "react";

const HomeSection = ({ heading, isLoading, movies }) => {
  const gridClasses =
    "grid grid-cols-1 sm:grid-cols-2 gap-4 lg:gap-6 items-start";

  return (
    <section className="grid">
      <h2 className="font-bold pb-2 md:pb-4 md:pt-4 text-xl md:text-2xl text-neutral-50">
        {heading}
      </h2>
      {isLoading ? (
        <div className={gridClasses}>
          {Array.from({ length: 8 }).map((_, index) => (
            <PosterCardSkeleton key={index} />
          ))}
        </div>
      ) : (
        <div className={gridClasses}>
          {movies.map((movie) => (
            <PosterCard
              key={movie.id}
              id={movie.id}
              image={`https://image.tmdb.org/t/p/original${movie.backdrop_path}`}
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
          className="bg-indigo-800 text-indigo-100 p-2 px-4 w-full md:w-max text-center rounded-md duration-300 hover:bg-indigo-700 font-medium"
        >
          View All
        </Link>
      </div>
    </section>
  );
};

export default function Home() {
  const [trendingMovies, setTrendingMovies] = useState([]);
  const [popularMovies, setPopularMovies] = useState([]);
  const [topRatedMovies, setTopRatedMovies] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const API_KEY = "e87b47516389ca897c5e6acdc3068cc2";
  const sectionsData = {
    "Popular Today": trendingMovies,
    Trending: popularMovies,
    "Top Rated": topRatedMovies,
  };

  const fetchData = async (endpoint) => {
    try {
      const data =
        (await fetch(
          `https://api.themoviedb.org/3${endpoint}?api_key=${API_KEY}`
        ).then((res) => res.json())) || [];
      return data.results
        .filter((result) => result.original_language !== "ru")
        .slice(0, 8);
    } catch (error) {
      console.log(error);
      return [];
    }
  };

  const fetchTrendingMovies = async () => {
    const data = await fetchData("/movie/now_playing");
    setTrendingMovies(data);
  };

  const fetchPopularMovies = async () => {
    const data = await fetchData("/movie/popular");
    setPopularMovies(data);
  };

  const fetchTopRatedMovies = async () => {
    const data = await fetchData("/movie/top_rated");
    setTopRatedMovies(data);
  };

  useEffect(() => {
    const fetchAll = async () => {
      await Promise.all([
        fetchTrendingMovies(),
        fetchPopularMovies(),
        fetchTopRatedMovies(),
      ]);
      setIsLoading(false);
    };

    fetchAll();
  }, []);

  return (
    <>
      <main className="grid p-4 gap-4 lg:gap-6 pb-16 max-w-6xl mx-auto">
        {Object.entries(sectionsData).map(([heading, movies]) => (
          <HomeSection
            key={heading}
            heading={heading}
            isLoading={isLoading}
            movies={movies}
          />
        ))}
      </main>
    </>
  );
}
