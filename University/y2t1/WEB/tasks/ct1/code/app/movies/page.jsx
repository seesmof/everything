"use client";
import Button from "@/components/Button";
import PageContainer from "@/components/PageContainer";
import PosterCard from "@/components/poster/PosterCard";
import PosterCardSkeleton from "@/components/poster/PosterCardSkeleton";
import { useRouter, useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";
import { FaChevronDown, FaChevronUp } from "react-icons/fa";

const Catalog = () => {
  const [movies, setMovies] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [page, setPage] = useState(1);
  const [ratingValue, setRatingValue] = useState(5);
  const [sorting, setSorting] = useState("popularity.desc");
  const [genres, setGenres] = useState([]);
  const [selectedGenres, setSelectedGenres] = useState([]);
  const [isGenreHidden, setIsGenreHidden] = useState(true);
  const searchParams = useSearchParams();

  const fetchMovies = async (page, sortBy, rating, inputGenres = []) => {
    setIsLoading(true);
    let genresString = inputGenres.map((genre) => genre.id).join(",");
    if (genresString === "") {
      genresString = "all";
    }
    const data = await fetch(
      `https://api.themoviedb.org/3/discover/movie?api_key=e87b47516389ca897c5e6acdc3068cc2&page=${page}&sort_by=${sortBy}&vote_average.gte=${rating}&with_genres=${genresString}`
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

  const handleGenreClick = (genre) => {
    setSelectedGenres((prevGenres) => {
      if (prevGenres.includes(genre)) {
        return prevGenres.filter((g) => g !== genre);
      } else {
        return [...prevGenres, genre];
      }
    });
  };

  useEffect(() => {
    const query = Number(searchParams.get("genre"));
    const genre = genres.find((genre) => genre.id === query);
    if (genre) {
      setSelectedGenres([genre]);
    }
    fetchMovies(page, sorting, ratingValue, selectedGenres);
  }, [genres]);

  useEffect(() => {
    Promise.all([fetchGenres()]).then(() => {
      setIsLoading(false);
    });
  }, []);

  useEffect(() => {
    Promise.all([fetchMovies(page, sorting, ratingValue, selectedGenres)]).then(
      () => {
        setIsLoading(false);
      }
    );
  }, [page, ratingValue, sorting, selectedGenres]);

  return (
    <>
      <PageContainer className="gap-4 lg:p-6 lg:gap-6 md:flex">
        <div className="grid gap-4 w-full md:w-[24%] h-min">
          <div className="grid gap-2">
            <label htmlFor="sorting" className="text-neutral-200 font-medium">
              Sorting
            </label>
            <select
              name="sorting"
              id="sorting"
              className="bg-neutral-800 hover:bg-neutral-700 focus:bg-neutral-700 p-2 rounded-lg"
              onChange={(e) => setSorting(e.target.value)}
            >
              <option value="popularity.desc">Popularity</option>
              <option value="vote_count.desc">Rating</option>
              <option value="revenue.desc">Revenue</option>
            </select>
          </div>
          <div className="grid">
            <label
              htmlFor="rating"
              className="text-neutral-200 font-medium pb-2"
            >
              Rating
            </label>
            <input
              id="rating"
              type="range"
              min="0"
              max="10"
              step="1"
              value={ratingValue}
              onChange={(e) => setRatingValue(e.target.value)}
              placeholder="Rating..."
              className="cursor-pointer"
            />
            <p className="text-neutral-300 text-sm font-medium pt-1">
              Starting from {ratingValue}/10
            </p>
          </div>
          <div className="grid gap-2">
            <div
              className="flex justify-between items-center cursor-pointer group"
              onClick={() => setIsGenreHidden(!isGenreHidden)}
            >
              <label
                htmlFor="genres"
                className="text-neutral-200 font-medium cursor-pointer"
              >
                Genres
              </label>
              {isGenreHidden ? (
                <FaChevronUp className="text-neutral-200" />
              ) : (
                <FaChevronDown className="text-neutral-200" />
              )}
            </div>
            <div className={`grid gap-2 ${isGenreHidden ? "hidden" : ""}`}>
              {genres.map((genre) => (
                <div key={genre.id} className="flex gap-2">
                  <input
                    type="checkbox"
                    id={genre.id}
                    name={genre.name}
                    value={genre.name}
                    className="accent-indigo-600"
                    checked={selectedGenres.some((g) => g.id === genre.id)}
                    onChange={() => handleGenreClick(genre.id)}
                  />
                  <label htmlFor={genre.id} className="text-neutral-200">
                    {genre.name}
                  </label>
                </div>
              ))}
            </div>
          </div>
        </div>
        <div className="gap-4 lg:gap-6 lg:p-6 grid flex-1">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {isLoading ? (
              <div className="h-[110vh] w-full"></div>
            ) : (
              movies.map((movie) => (
                <PosterCard
                  key={movie.id}
                  id={movie.id}
                  image={`https://image.tmdb.org/t/p/original${movie.backdrop_path}`}
                  name={movie.title}
                  release_year={movie.release_date.slice(0, 4)}
                  media_type="movie"
                  rating={movie.vote_average}
                />
              ))
            )}
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
