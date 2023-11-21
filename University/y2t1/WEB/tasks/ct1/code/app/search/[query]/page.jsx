"use client";
import Button from "@/components/Button";
import Input from "@/components/Input";
import PosterCard from "@/components/poster/PosterCard";
import PosterCardSkeleton from "@/components/poster/PosterCardSkeleton";
import Link from "next/link";
import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import { MdKeyboardDoubleArrowUp } from "react-icons/md";

const SearchResults = () => {
  const { query } = useParams();
  const [searchQuery, setSearchQuery] = useState(query);
  const [searchResults, setSearchResults] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const fetchSearch = async () => {
    setIsLoading(true);
    const data = await fetch(
      `https://api.themoviedb.org/3/search/movie?api_key=e87b47516389ca897c5e6acdc3068cc2&query=${searchQuery}`
    ).then((res) => res.json());
    setSearchResults(
      data.results
        .filter((result) => result.original_language !== "ru")
        .filter((result) => result.backdrop_path && result.poster_path)
        .filter((result) => result.overview && result.overview.trim() !== "")
        .filter((result) => result.vote_average > 0)
    );
    setIsLoading(false);
  };

  useEffect(() => {
    Promise.all([fetchSearch()]).then(() => {
      setIsLoading(false);
    });
  }, []);

  return (
    <>
      <div className="mx-auto max-w-6xl p-4 grid pb-20">
        <div className="flex items-center gap-2" id="page-top">
          <Input
            className="w-full"
            type="text"
            placeholder="Retry search..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === "Enter") {
                setSearchQuery(searchQuery);
                fetchSearch();
              }
            }}
          />
          <Button
            type="submit"
            onClick={() => {
              setSearchQuery(searchQuery);
              fetchSearch();
            }}
          >
            Retry
          </Button>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4 md:gap-6">
          {isLoading ? (
            Array.from({ length: 8 }).map((_, index) => (
              <PosterCardSkeleton key={index} />
            ))
          ) : searchResults.length === 0 ? (
            <div className="flex justify-center items-center py-80 col-span-full">
              <h1 className="text-2xl font-bold">No results found</h1>
            </div>
          ) : (
            searchResults.map((movie) => (
              <PosterCard
                key={movie.id}
                id={movie.id}
                image={`https://image.tmdb.org/t/p/original${movie.backdrop_path}`}
                name={movie.title}
                media_type={movie.media_type}
                release_year={movie.release_date?.slice(0, 4)}
                rating={movie.vote_average}
              />
            ))
          )}
        </div>
        <div className="flex justify-end mt-4">
          <Button className="w-max text-xl">
            <Link href={`/search/${searchQuery}#page-top`}>
              <MdKeyboardDoubleArrowUp />
            </Link>
          </Button>
        </div>
      </div>
    </>
  );
};

export default SearchResults;
