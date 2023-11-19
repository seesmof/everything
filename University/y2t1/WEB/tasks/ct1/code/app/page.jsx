const Main = () => {
  return (
    <>
      <div className="p-4 grid grid-cols-1 gap-4 mb-14 md:mb-0 max-w-6xl mx-auto">
        <div className="w-full aspect-square rounded-md bg-sky-500"></div>
        <div className="w-full aspect-square rounded-md bg-yellow-500"></div>
        <div className="w-full aspect-square rounded-md bg-sky-500"></div>
        <div className="w-full aspect-square rounded-md bg-yellow-500"></div>
        <div className="w-full aspect-square rounded-md bg-sky-500"></div>
        <div className="w-full aspect-square rounded-md bg-yellow-500"></div>
      </div>
    </>
  );
};

export default function Home() {
  return (
    <>
      <Main />
    </>
  );
}
