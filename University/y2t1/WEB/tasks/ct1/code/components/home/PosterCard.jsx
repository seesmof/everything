import Link from "next/link";

const PosterCard = ({ image, name, media_type, release_year, id }) => {
  return (
    <>
      <Link href="/[id]" as={`/${id}`} className="grid gap-2">
        <div className="w-full rounded-md overflow-hidden">
          <img
            src={image}
            className="w-full max-h-96 md:max-h-[22rem] object-cover"
            alt="Poster image"
          />
        </div>
        <div className="flex flex-col text-slate-200">
          <div className="flex flex-row gap-2 mt-1 text-sm">
            <p>{media_type === "tv" ? "Show" : "Movie"}</p>
            <p className="text-slate-300 scale-90">•</p>
            <p>{release_year}</p>
          </div>
          <p className="text-lg md:text-xl font-medium text-slate-100 md:mt-1">
            {name}
          </p>
        </div>
      </Link>
    </>
  );
};

export default PosterCard;
