import React from "react";

const PosterCardSkeleton = () => {
  return (
    <>
      <div className="grid gap-2">
        <div className="w-full rounded-md overflow-hidden h-96 animate-pulse bg-slate-700"></div>
        <div className="flex flex-col">
          <div className="rounded-md bg-slate-700 animate-pulse w-12 h-3"></div>
          <div className="rounded-md bg-slate-700 animate-pulse w-36 h-6 mt-2"></div>
        </div>
      </div>
    </>
  );
};

export default PosterCardSkeleton;
