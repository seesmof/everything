"use client";
import Link from "next/link";
import { useEffect, useState } from "react";

const PosterCard = ({ image, name, media_type, release_year }) => {
  return (
    <>
      <Link href={`/catalog/${name}`} className="grid gap-2">
        <div className="w-full rounded-md overflow-hidden">
          <img
            src={image}
            className="w-full max-h-96 md:max-h-[22rem] object-cover"
            alt="Poster image"
          />
        </div>
        <div className="flex flex-col text-slate-200">
          <div className="flex flex-row gap-2 mt-1 text-sm">
            <p>{media_type === "tv" ? "Show" : "Movie"}</p>
            <p className="text-slate-300 scale-90">•</p>
            <p>{release_year}</p>
          </div>
          <p className="text-lg md:text-xl font-medium text-slate-100 md:mt-1">
            {name}
          </p>
        </div>
      </Link>
    </>
  );
};

const PosterCardSkeleton = () => {
  return (
    <>
      <div className="grid gap-2">
        <div className="w-full rounded-md overflow-hidden h-96 animate-pulse bg-slate-700"></div>
        <div className="flex flex-col">
          <div className="rounded-md bg-slate-700 animate-pulse w-12 h-3"></div>
          <div className="rounded-md bg-slate-700 animate-pulse w-36 h-6 mt-2"></div>
        </div>
      </div>
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
      `https://api.themoviedb.org/3/trending/tv/day?api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    let filteredData = data.results.filter(
      (result) => result.original_language !== "ru"
    );
    filteredData = filteredData.slice(0, 4);
    console.log(filteredData);
    setTrendingShows(filteredData);
  };

  const fetchTrendingMovies = async () => {
    const res = await fetch(
      `https://api.themoviedb.org/3/trending/movie/day?api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    let filteredData = data.results.filter(
      (result) => result.original_language !== "ru"
    );
    filteredData = filteredData.slice(0, 4);
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
    filteredData = filteredData.slice(0, 4);
    console.log(filteredData);
    setPopularMovies(filteredData);
  };

  const fetchPopularShows = async () => {
    const res = await fetch(
      `https://api.themoviedb.org/3/tv/popular?api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    let filteredData = data.results.filter(
      (result) => result.original_language !== "ru"
    );
    filteredData = filteredData.slice(0, 4);
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
      <div className="grid p-4 gap-4 pb-16 max-w-6xl mx-auto">
        <div className="grid">
          <h2 className="font-bold pb-2 md:pb-4 md:pt-4 text-xl md:text-2xl text-slate-50">
            Trending Movies
          </h2>
          {isLoading ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
              {Array.from({ length: 4 }).map((_, index) => (
                <PosterCardSkeleton key={index} />
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
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
          <div className="flex md:justify-end mt-2 mb-2">
            <Link
              href={"/movies"}
              className="bg-slate-800 text-slate-300 p-2 px-4 w-full md:w-max text-center rounded-md duration-300 hover:bg-slate-700"
            >
              View All
            </Link>
          </div>
        </div>
        <div className="grid">
          <h2 className="font-bold pb-2 md:pb-4 md:pt-4 text-xl md:text-2xl text-slate-50">
            Popular Movies
          </h2>
          {isLoading ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
              {Array.from({ length: 4 }).map((_, index) => (
                <PosterCardSkeleton key={index} />
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
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
          <div className="flex md:justify-end mt-2 mb-2">
            <Link
              href={"/movies"}
              className="bg-slate-800 text-slate-300 p-2 px-4 w-full md:w-max text-center rounded-md duration-300 hover:bg-slate-700"
            >
              View All
            </Link>
          </div>
        </div>
        <div className="grid">
          <h2 className="font-bold pb-2 md:pb-4 md:pt-4 text-xl md:text-2xl text-slate-50">
            Trending Shows
          </h2>
          {isLoading ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
              {Array.from({ length: 4 }).map((_, index) => (
                <PosterCardSkeleton key={index} />
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
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
          <div className="flex md:justify-end mt-2 mb-2">
            <Link
              href={"/movies"}
              className="bg-slate-800 text-slate-300 p-2 px-4 w-full md:w-max text-center rounded-md duration-300 hover:bg-slate-700"
            >
              View All
            </Link>
          </div>
        </div>
        <div className="grid">
          <h2 className="font-bold pb-2 md:pb-4 md:pt-4 text-xl md:text-2xl text-slate-50">
            Popular Shows
          </h2>
          {isLoading ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
              {Array.from({ length: 4 }).map((_, index) => (
                <PosterCardSkeleton key={index} />
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 items-start">
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
          <div className="flex md:justify-end mt-2 mb-2">
            <Link
              href={"/movies"}
              className="bg-slate-800 text-slate-300 p-2 px-4 w-full md:w-max text-center rounded-md duration-300 hover:bg-slate-700"
            >
              View All
            </Link>
          </div>
        </div>
      </div>
    </>
  );
}
