"use client";
import HomeSection from "@/components/home/HomeSection";
import { useEffect, useState } from "react";

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
