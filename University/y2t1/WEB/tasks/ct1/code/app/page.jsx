"use client";
import Link from "next/link";
import { useEffect, useState } from "react";

const PosterCard = ({
  image,
  name,
  vote_average,
  media_type,
  release_year,
}) => {
  return (
    <>
      <Link href={`/catalog/${name}`} className="grid gap-2">
        <div className="w-full rounded-md overflow-hidden">
          <img
            src={image}
            className="w-full h-full object-cover"
            alt="Poster image"
          />
        </div>
        <div className="flex flex-col text-slate-200">
          <div className="flex flex-row gap-2 mt-1 text-sm">
            <p>{media_type === "tv" ? "Show" : "Movie"}</p>
            <p className="text-slate-300 scale-90">•</p>
            <p>{release_year}</p>
          </div>
          <p className="text-xl font-medium text-slate-50 mt-1 md:mt-2">
            {name}
          </p>
        </div>
      </Link>
    </>
  );
};

export default function Home() {
  const [trendingShows, setTrendingShows] = useState([]);
  const [trendingMovies, setTrendingMovies] = useState([]);
  const [popularMovies, setPopularMovies] = useState([]);
  const [popularShows, setPopularShows] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const fetchTrendingShows = async () => {
    const res = await fetch(
      `https://api.themoviedb.org/3/trending/tv/week?api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    const filteredData = data.results.filter(
      (result) => result.original_language !== "ru"
    );
    console.log(filteredData);
    setTrendingShows(filteredData);
  };

  const fetchTrendingMovies = async () => {
    const res = await fetch(
      `https://api.themoviedb.org/3/trending/movie/week?api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    const filteredData = data.results.filter(
      (result) => result.original_language !== "ru"
    );
    console.log(filteredData);
    setTrendingMovies(filteredData);
  };

  const fetchPopularMovies = async () => {
    const res = await fetch(
      `https://api.themoviedb.org/3/movie/popular?api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    const filteredData = data.results.filter(
      (result) => result.original_language !== "ru"
    );
    console.log(filteredData);
    setPopularMovies(filteredData);
  };

  const fetchPopularShows = async () => {
    const res = await fetch(
      `https://api.themoviedb.org/3/tv/popular?api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    const filteredData = data.results.filter(
      (result) => result.original_language !== "ru"
    );
    console.log(filteredData);
    setPopularShows(filteredData);
  };

  useEffect(() => {
    Promise.all([
      fetchTrendingMovies(),
      fetchTrendingShows(),
      fetchPopularMovies(),
      fetchPopularShows(),
    ]).then(() => {
      setIsLoading(false);
    });
  }, []);

  return (
    <>
      <div className="grid p-4 gap-4 max-w-6xl mx-auto">
        <div className="grid">
          <h2 className="font-medium pb-4 text-xl md:text-2xl">
            Trending Movies
          </h2>
          {isLoading ? (
            <p>Loading...</p>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              {trendingMovies.map((movie) => (
                <PosterCard
                  key={movie.id}
                  image={`https://image.tmdb.org/t/p/original${movie.poster_path}`}
                  name={movie.title}
                  release_year={movie.release_date.slice(0, 4)}
                  media_type="movie"
                />
              ))}
            </div>
          )}
        </div>
        <div className="grid">
          <h2 className="font-medium pb-4 text-xl md:text-2xl">
            Trending Shows
          </h2>
          {isLoading ? (
            <p>Loading...</p>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              {trendingShows.map((show) => (
                <PosterCard
                  key={show.id}
                  image={`https://image.tmdb.org/t/p/original${show.poster_path}`}
                  name={show.name}
                  release_year={show.first_air_date.slice(0, 4)}
                  media_type="tv"
                />
              ))}
            </div>
          )}
        </div>
        <div className="grid">
          <h2 className="font-medium pb-4 text-xl md:text-2xl">
            Popular Movies
          </h2>
          {isLoading ? (
            <p>Loading...</p>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              {popularMovies.map((movie) => (
                <PosterCard
                  key={movie.id}
                  image={`https://image.tmdb.org/t/p/original${movie.poster_path}`}
                  name={movie.title}
                  release_year={movie.release_date.slice(0, 4)}
                  media_type="movie"
                />
              ))}
            </div>
          )}
        </div>
        <div className="grid">
          <h2 className="font-medium pb-4 text-xl md:text-2xl">
            Popular Shows
          </h2>
          {isLoading ? (
            <p>Loading...</p>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              {popularShows.map((show) => (
                <PosterCard
                  key={show.id}
                  image={`https://image.tmdb.org/t/p/original${show.poster_path}`}
                  name={show.name}
                  release_year={show.first_air_date.slice(0, 4)}
                  media_type="tv"
                />
              ))}
            </div>
          )}
        </div>
      </div>
    </>
  );
}
