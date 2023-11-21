import Link from "next/link";
import PosterCard from "../poster/PosterCard";
import PosterCardSkeleton from "../poster/PosterCardSkeleton";
import Button from "../Button";

const HomeSection = ({ heading, isLoading, movies }) => {
  const gridClasses =
    "grid grid-cols-1 sm:grid-cols-2 gap-4 lg:gap-6 items-start";

  return (
    <section className="grid">
      <h2 className="font-bold pb-2 md:pb-4 md:pt-4 text-xl md:text-2xl text-neutral-50">
        {heading}
      </h2>
      {isLoading ? (
        <div className={gridClasses}>
          {Array.from({ length: 8 }).map((_, index) => (
            <PosterCardSkeleton key={index} />
          ))}
        </div>
      ) : (
        <div className={gridClasses}>
          {movies.map((movie) => (
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
      )}
      <div className="flex md:justify-end mt-2 mb-2">
        <Button className="w-full md:w-max bg-indigo-800 hover:bg-indigo-700 border-indigo-800 hover:border-indigo-700 md:mt-2">
          <Link href={"/movies"}>View All</Link>
        </Button>
      </div>
    </section>
  );
};

export default HomeSection;
