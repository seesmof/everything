const MovieTemplateSkeleton = () => {
  return (
    <main className="grid p-4 lg:p-6">
      <div className="w-full hidden md:block md:h-96 rounded-md bg-neutral-700 animate-pulse"></div>
      <div className="grid gap-4 lg:gap-6 xl:gap-8 md:flex md:pt-4 lg:pt-6">
        <div className="w-1/3 h-72 md:h-96 rounded-md bg-neutral-700 animate-pulse"></div>
        <div className="flex-1 flex flex-col gap-2">
          <div className="bg-neutral-700 animate-pulse h-4 rounded-md w-24"></div>
          <div className="bg-neutral-700 animate-pulse h-8 rounded-md w-48"></div>
          <div className="bg-neutral-700 animate-pulse h-32 rounded-md w-96"></div>
          <div className="bg-neutral-700 animate-pulse h-4 rounded-md w-24"></div>
        </div>
      </div>
    </main>
  );
};

export default MovieTemplateSkeleton;
