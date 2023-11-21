import Link from "next/link";
import PosterCard from "../poster/PosterCard";
import PosterCardSkeleton from "../poster/PosterCardSkeleton";

const HomeSection = ({ heading, isLoading, movies }) => {
  const gridClasses =
    "grid grid-cols-1 sm:grid-cols-2 gap-4 lg:gap-6 items-start";

  return (
    <section className="grid">
      <div className="flex items-center justify-between">
        <h2 className="font-bold pb-2 md:pb-4 md:pt-4 text-xl md:text-2xl text-neutral-50">
          {heading}
        </h2>
        <Link
          href={`/movies`}
          className="text-sm text-neutral-300 duration-300 hover:text-neutral-50"
        >
          View All
        </Link>
      </div>
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
    </section>
  );
};

export default HomeSection;
