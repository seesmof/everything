"use client";
import PageContainer from "@/components/PageContainer";
import PosterCard from "@/components/poster/PosterCard";
import PosterCardSkeleton from "@/components/poster/PosterCardSkeleton";
import { useEffect, useState } from "react";

const Catalog = () => {
  const [movies, setMovies] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const fetchMovies = async () => {
    const data = await fetch(
      `https://api.themoviedb.org/3/discover/movie?api_key=e87b47516389ca897c5e6acdc3068cc2`
    ).then((res) => res.json());
    setMovies(data.results);
  };

  useEffect(() => {
    Promise.all([fetchMovies()]).then(() => {
      setIsLoading(false);
    });
  }, []);

  return (
    <>
      <PageContainer className="gap-4 lg:gap-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {isLoading
            ? Array.from({ length: 8 }).map((_, index) => (
                <PosterCardSkeleton key={index} />
              ))
            : movies.map((movie) => (
                <PosterCard
                  key={movie.id}
                  id={movie.id}
                  image={`https://image.tmdb.org/t/p/original${movie.backdrop_path}`}
                  name={movie.title}
                  release_year={movie.release_date.slice(0, 4)}
                  media_type="movie"
                  rating={movie.vote_average}
                />
              ))}
        </div>
      </PageContainer>
    </>
  );
};

export default Catalog;
