"use client";
import PosterCard from "@/components/home/PosterCard";
import Link from "next/link";
import { useParams } from "next/navigation";
import { useEffect, useState } from "react";

const MovieTemplate = ({
  name,
  description,
  year,
  runtime,
  rating,
  image,
  backdrop,
  genres,
  id,
  imdbId,
}) => {
  const [similarMovies, setSimilarMovies] = useState([]);

  const fetchSimilarMovies = async () => {
    const res = await fetch(
      `https://api.themoviedb.org/3/movie/${id}/similar?api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    setSimilarMovies(data.results.slice(0, 4));
  };

  useEffect(() => {
    fetchSimilarMovies();
  }, []);

  return (
    <>
      <main className="grid p-4 text-neutral-200">
        <img
          src={backdrop}
          alt="Movie backdrop"
          className="w-full max-h-96 object-cover object-top rounded-md"
        />
        <div className="grid gap-4 lg:gap-6 xl:gap-8 md:flex md:pt-4 lg:pt-6">
          <div className="grid">
            <img
              src={image}
              alt="Movie poster"
              className="w-full hidden md:block max-h-96 max-w-sm md:max-h-max object-cover rounded-md"
            />
          </div>
          <div className="grid flex-1">
            <div className="flex items-center gap-3">
              <p>{genres[0].name}</p>
              <p className="text-indigo-500 scale-90">•</p>
              <p>{year}</p>
            </div>
            <div className="flex items-center justify-between pb-4 pt-2 md:pt-1">
              <h1 className="font-bold md:text-4xl text-2xl text-neutral-50">
                {name}
              </h1>
              <p
                className={`text-neutral-50 font-medium rounded-md p-1 px-4 ${
                  rating >= 8
                    ? "bg-green-600"
                    : rating <= 3
                    ? "bg-red-600"
                    : "bg-indigo-700"
                }`}
              >
                {Math.round(rating * 10) / 10}
              </p>
            </div>
            <p>{description}</p>
            <p className="text-neutral-50 mt-2 mb-4 font-medium">
              Movie length: {Math.floor(runtime / 60)}h {runtime % 60}m
            </p>
            <div className="flex items-center gap-2 justify-end">
              <Link
                href={`https://letterboxd.com/film/${name
                  .replace(" ", "-")
                  .toLowerCase()}/`}
                className="bg-indigo-900 font-medium px-4 py-2 rounded-md duration-300 hover:text-white text-neutral-50 hover:bg-indigo-700"
              >
                Letterboxd
              </Link>
              <Link
                className="bg-indigo-900 font-medium px-4 py-2 rounded-md duration-300 hover:text-white text-neutral-50 hover:bg-indigo-700"
                href={`https://www.imdb.com/title/${imdbId}/`}
              >
                IMDb
              </Link>
            </div>
            <h2 className="font-medium text-lg md:text-xl pb-2 pt-4 md:pb-4 text-neutral-50">
              Similar Movies
            </h2>
            <div className="grid gap-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-4 mb-12 items-start">
              {similarMovies.map((movie) => (
                <PosterCard
                  key={movie.id}
                  image={`https://image.tmdb.org/t/p/original${movie.poster_path}`}
                  name={movie.title}
                  media_type={movie.media_type}
                  release_year={movie.release_date?.slice(0, 4)}
                  id={movie.id}
                />
              ))}
            </div>
          </div>
        </div>
      </main>
    </>
  );
};

const MovieTemplateSkeleton = () => {
  return (
    <main className="grid p-4 lg:p-6">
      <div className="w-full hidden md:block md:h-96 rounded-md bg-neutral-700 animate-pulse"></div>
      <div className="grid gap-4 lg:gap-6 xl:gap-8 md:flex md:pt-4 lg:pt-6">
        <div className="w-1/3 h-72 md:h-96 rounded-md bg-neutral-700 animate-pulse"></div>
        <div className="flex-1 flex flex-col gap-2">
          <div className="bg-neutral-700 animate-pulse h-4 rounded-md w-24"></div>
          <div className="bg-neutral-700 animate-pulse h-8 rounded-md w-48"></div>
          <div className="bg-neutral-700 animate-pulse h-32 rounded-md w-96"></div>
          <div className="bg-neutral-700 animate-pulse h-4 rounded-md w-24"></div>
        </div>
      </div>
    </main>
  );
};

const Movie = () => {
  const [movie, setMovie] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const { id } = useParams();

  const fetchMovie = async () => {
    const res = await fetch(
      `https://api.themoviedb.org/3/movie/${id}?api_key=e87b47516389ca897c5e6acdc3068cc2`
    );
    const data = await res.json();
    console.log(data);
    setMovie(data);
  };

  useEffect(() => {
    Promise.all([fetchMovie()]).then(() => {
      setIsLoading(false);
    });
  }, []);

  return (
    <>
      <div className="mx-auto max-w-6xl">
        {isLoading ? (
          <MovieTemplateSkeleton />
        ) : (
          <MovieTemplate
            name={movie.title}
            description={movie.overview}
            year={movie.release_date?.slice(0, 4)}
            runtime={movie.runtime}
            rating={movie.vote_average}
            image={`https://image.tmdb.org/t/p/original${movie.poster_path}`}
            backdrop={`https://image.tmdb.org/t/p/original${movie.backdrop_path}`}
            genres={movie.genres}
            id={movie.id}
            imdbId={movie.imdb_id}
          />
        )}
      </div>
    </>
  );
};

export default Movie;
