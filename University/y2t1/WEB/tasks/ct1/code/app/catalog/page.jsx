"use client";
import Button from "@/components/Button";
import PageContainer from "@/components/PageContainer";
import PosterCard from "@/components/poster/PosterCard";
import PosterCardSkeleton from "@/components/poster/PosterCardSkeleton";
import { useEffect, useState } from "react";

const Catalog = () => {
  const [movies, setMovies] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [page, setPage] = useState(1);

  const fetchMovies = async (page) => {
    setIsLoading(true);
    const data = await fetch(
      `https://api.themoviedb.org/3/discover/movie?api_key=e87b47516389ca897c5e6acdc3068cc2&page=${page}`
    ).then((res) => res.json());
    setMovies(
      data.results
        .filter((result) => result.original_language !== "ru")
        .filter((result) => result.backdrop_path && result.poster_path)
        .filter((result) => result.overview && result.overview.trim() !== "")
        .filter((result) => result.vote_average > 0)
    );
    setIsLoading(false);
  };

  useEffect(() => {
    Promise.all([fetchMovies(page)]).then(() => {
      setIsLoading(false);
    });
  }, [page]);

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
        <div className="flex items-center justify-between mt-2">
          <Button
            onClick={() => {
              if (page > 1) {
                setPage(page - 1);
              }
            }}
            disabled={page === 1}
            className={`disabled:cursor-not-allowed disabled:opacity-70 disabled:active:scale-100`}
          >
            Back
          </Button>
          <div className="text-sm text-neutral-300 font-medium flex">
            Page {page}
          </div>
          <Button
            onClick={() => {
              if (page <= 500) {
                setPage(page + 1);
              }
            }}
            disabled={page === 500}
            className={`disabled:cursor-not-allowed disabled:opacity-70 disabled:active:scale-100`}
          >
            Next
          </Button>
        </div>
      </PageContainer>
    </>
  );
};

export default Catalog;
