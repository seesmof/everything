"use client";
import MovieTemplate from "@/components/movie-details/MovieTemplate";
import MovieTemplateSkeleton from "@/components/movie-details/MovieTemplateSkeleton";
import { useParams } from "next/navigation";
import { useEffect, useState } from "react";

const Movie = () => {
  const [movie, setMovie] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const { id } = useParams();

  const fetchMovie = async () => {
    const data = await fetch(
      `https://api.themoviedb.org/3/movie/${id}?api_key=${process.env.TMDB_API_KEY}`
    ).then((res) => res.json());
    setMovie(data);
  };

  useEffect(() => {
    Promise.all([fetchMovie()]).then(() => {
      setIsLoading(false);
    });
  }, []);

  return (
    <>
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
    </>
  );
};

export default Movie;
