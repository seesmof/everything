"use client";
import Button from "@/components/Button";
import PageContainer from "@/components/PageContainer";
import PosterCard from "@/components/poster/PosterCard";
import PosterCardSkeleton from "@/components/poster/PosterCardSkeleton";
import { useEffect, useState } from "react";
import { FaChevronDown, FaChevronUp } from "react-icons/fa";

const Catalog = () => {
  const [movies, setMovies] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [page, setPage] = useState(1);
  const [genres, setGenres] = useState([]);
  const [isGenresCollapsed, setIsGenresCollapsed] = useState(true);
  const [ratingMin, setRatingMin] = useState(0);
  const [ratingMax, setRatingMax] = useState(10);
  const [searchQuery, setSearchQuery] = useState("");

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

  const fetchGenres = async () => {
    setIsLoading(true);
    const data = (
      await fetch(
        `https://api.themoviedb.org/3/genre/movie/list?language=en&api_key=e87b47516389ca897c5e6acdc3068cc2`
      ).then((res) => res.json())
    ).genres;
    setGenres(data);
    setIsLoading(false);
  };

  useEffect(() => {
    Promise.all([fetchGenres()]).then(() => {
      setIsLoading(false);
    });
  }, []);

  useEffect(() => {
    Promise.all([fetchMovies(page)]).then(() => {
      setIsLoading(false);
    });
  }, [page]);

  return (
    <>
      <PageContainer className="gap-4 lg:p-6 lg:gap-6 md:flex">
        <div className="grid gap-4 w-full md:w-1/3 h-min">
          <div className="grid gap-2">
            <label htmlFor="search" className="text-neutral-200 font-medium">
              Search
            </label>
            <input
              id="search"
              type="text"
              className="w-full p-2 rounded-lg bg-neutral-800 hover:bg-neutral-700 focus:bg-neutral-700"
              placeholder="Movie name..."
            />
          </div>
          <div className="grid gap-2">
            <label htmlFor="year" className="text-neutral-200 font-medium">
              Release Year
            </label>
            <input
              id="year"
              type="text"
              className="w-full p-2 rounded-lg bg-neutral-800 hover:bg-neutral-700 focus:bg-neutral-700"
              placeholder="Release year..."
            />
          </div>
          <div className="grid gap-2">
            <label htmlFor="sorting" className="text-neutral-200 font-medium">
              Sorting
            </label>
            <select
              name="sorting"
              id="sorting"
              className="bg-neutral-800 hover:bg-neutral-700 focus:bg-neutral-700 p-2 rounded-lg"
            >
              <option value="popularity.desc">Popularity</option>
              <option value="release_date.desc">Release Date</option>
              <option value="vote_average.desc">Rating</option>
            </select>
          </div>
          <div className="grid">
            <label
              htmlFor="rating"
              className="text-neutral-200 font-medium pb-1"
            >
              Rating
            </label>
            <input
              id="rating"
              type="range"
              min="0"
              max="10"
              step="1"
              className="w-full p-2 rounded-lg bg-neutral-800 hover:bg-neutral-700 focus:bg-neutral-700"
              placeholder="Rating..."
            />
            <div className="flex justify-between items-center text-sm text-neutral-300 font-medium">
              <input
                type="text"
                value={ratingMin}
                onChange={(e) => setRatingMin(e.target.value)}
                className="bg-neutral-800 hover:bg-neutral-700 focus:bg-neutral-700 p-1.5 max-w-[2rem] rounded-lg"
              />
              <input
                type="text"
                value={ratingMax}
                onChange={(e) => setRatingMin(e.target.value)}
                className="bg-neutral-800 hover:bg-neutral-700 focus:bg-neutral-700 p-1.5 max-w-[2rem] rounded-lg"
              />
            </div>
          </div>
          <div className="grid gap-2">
            <div
              className="flex justify-between items-center cursor-pointer group"
              onClick={() => setIsGenresCollapsed(!isGenresCollapsed)}
            >
              <label
                htmlFor="genres"
                className="text-neutral-200 font-medium cursor-pointer"
              >
                Genres
              </label>
              {isGenresCollapsed ? (
                <FaChevronUp className="text-neutral-200" />
              ) : (
                <FaChevronDown className="text-neutral-200" />
              )}
            </div>
            <div className={`grid gap-2 ${isGenresCollapsed ? "hidden" : ""}`}>
              {genres.map((genre) => (
                <div key={genre.id} className="flex gap-2">
                  <input
                    type="checkbox"
                    id={genre.id}
                    name={genre.name}
                    value={genre.name}
                    className="accent-indigo-600"
                  />
                  <label htmlFor={genre.id} className="text-neutral-200">
                    {genre.name}
                  </label>
                </div>
              ))}
            </div>
          </div>
        </div>
        <div className="gap-4 lg:gap-6 lg:p-6 grid">
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
        </div>
      </PageContainer>
    </>
  );
};

export default Catalog;
