import PageContainer from "../PageContainer";

const MovieTemplateSkeleton = () => {
  return (
    <PageContainer>
      <div className="w-full hidden md:block md:h-96 rounded-xl bg-neutral-700 animate-pulse"></div>
      <div className="grid gap-4 lg:gap-6 xl:gap-8 md:flex md:pt-4 lg:pt-6">
        <div className="w-1/3 max-w-sm h-[50vh] rounded-xl bg-neutral-700 animate-pulse"></div>
        <div className="flex-1 flex flex-col gap-2">
          <div className="bg-neutral-700 animate-pulse h-4 rounded-xl w-24"></div>
          <div className="bg-neutral-700 animate-pulse h-8 rounded-xl w-48"></div>
          <div className="bg-neutral-700 animate-pulse h-32 rounded-xl w-96"></div>
          <div className="bg-neutral-700 animate-pulse h-4 rounded-xl w-24"></div>
        </div>
      </div>
    </PageContainer>
  );
};

export default MovieTemplateSkeleton;
