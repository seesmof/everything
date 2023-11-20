import Link from "next/link";
import PosterCard from "../poster/PosterCard";
import PosterCardSkeleton from "../poster/PosterCardSkeleton";

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
        <Link
          href={"/movies"}
          className="bg-indigo-800 text-indigo-100 p-2 px-4 w-full md:w-max text-center rounded-xl duration-300 hover:bg-indigo-700 font-medium"
        >
          View All
        </Link>
      </div>
    </section>
  );
};

export default HomeSection;
