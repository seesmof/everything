import Image from "next/image";
import Link from "next/link";

const PosterCard = ({ image, name, media_type, release_year, id, rating }) => {
  return (
    <>
      <Link href="/movies/[id]" as={`/movies/${id}`} className="grid gap-2">
        <div className="relative duration-300 active:scale-95 group w-full rounded-xl overflow-hidden mb-1">
          <div className="absolute inset-0 bg-neutral-800 group-hover:bg-opacity-50 bg-opacity-0 duration-300 w-full h-full flex items-center justify-center">
            <p
              className={
                "group-hover:opacity-100 opacity-0 text-white font-bold duration-300 text-xl"
              }
            >
              {Math.round(rating * 10) / 10}
            </p>
          </div>
          <img
            src={image}
            className="w-full max-h-96 object-cover z-20"
            alt="Poster image"
          />
        </div>
        <main className="grid text-neutral-200">
          <div className="flex gap-2 text-sm">
            <p>{media_type === "tv" ? "Show" : "Movie"}</p>
            <p className="text-indigo-500 scale-90">•</p>
            <p>{release_year}</p>
          </div>
          <h3 className="text-lg md:text-xl font-medium text-neutral-100 hover:text-indigo-400 duration-300 md:mt-1">
            {name}
          </h3>
        </main>
      </Link>
    </>
  );
};

export default PosterCard;
