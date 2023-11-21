"use client";
import Button from "@/components/Button";
import Input from "@/components/Input";
import PageContainer from "@/components/PageContainer";
import HomeSection from "@/components/home/HomeSection";
import PosterCard from "@/components/poster/PosterCard";
import PosterCardSkeleton from "@/components/poster/PosterCardSkeleton";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function Home() {
  const [trendingMovies, setTrendingMovies] = useState([]);
  const [popularMovies, setPopularMovies] = useState([]);
  const [topRatedMovies, setTopRatedMovies] = useState([]);
  const [movieOfDay, setMovieOfDay] = useState({});
  const [isLoading, setIsLoading] = useState(true);
  const API_KEY = "e87b47516389ca897c5e6acdc3068cc2";
  const sectionsData = {
    "Popular Today": trendingMovies,
    Trending: popularMovies,
    "Top Rated": topRatedMovies,
  };
  const [searchQuery, setSearchQuery] = useState("");
  const router = useRouter();

  const handleSearch = (event) => {
    event.preventDefault();
    router.push(`/search/${searchQuery}`);
    setSearchQuery("");
  };

  const fetchData = async (endpoint) => {
    try {
      const data =
        (await fetch(
          `https://api.themoviedb.org/3${endpoint}?api_key=${API_KEY}`
        ).then((res) => res.json())) || [];
      return data.results
        .filter((result) => result.original_language !== "ru")
        .filter((result) => result.backdrop_path && result.poster_path)
        .filter((result) => result.overview && result.overview.trim() !== "")
        .filter((result) => result.vote_average > 0)
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
    const randomMovie = data[Math.floor(Math.random() * data.length)];
    setMovieOfDay(randomMovie);
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
      <PageContainer className="gap-4 lg:gap-6">
        <div className="grid">
          <h2 className="font-bold text-2xl md:text-3xl pb-2 md:pb-4">
            Movie of Today
          </h2>
          {isLoading ? (
            <PosterCardSkeleton />
          ) : (
            <PosterCard
              image={`https://image.tmdb.org/t/p/original${movieOfDay.backdrop_path}`}
              name={movieOfDay.title}
              media_type="movie"
              release_year={movieOfDay.release_date.slice(0, 4)}
              id={movieOfDay.id}
              rating={movieOfDay.vote_average}
            />
          )}
        </div>
        <div className="flex items-center gap-2">
          <Input
            className="w-full"
            type="text"
            placeholder="Search movies..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === "Enter") {
                setSearchQuery(searchQuery);
                router.push(`/search/${searchQuery}`);
              }
            }}
          />
          <Button type="submit" onClick={handleSearch}>
            Search
          </Button>
        </div>
        {Object.entries(sectionsData).map(([heading, movies]) => (
          <HomeSection
            key={heading}
            heading={heading}
            isLoading={isLoading}
            movies={movies}
          />
        ))}
      </PageContainer>
    </>
  );
}
