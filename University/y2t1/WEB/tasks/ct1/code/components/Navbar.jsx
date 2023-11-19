import Link from "next/link";

const Navbar = () => {
  return (
    <>
      <nav className="bg-slate-800 text-slate-300 fixed bottom-0 left-0 right-0 md:sticky md:top-0">
        <div className="flex items-center justify-between p-2 gap-2 md:hidden">
          <Link
            href={"/"}
            className="p-2 grow rounded-md hover:bg-slate-700 hover:text-white active:text-white active:bg-slate-600 duration-300"
          >
            Home
          </Link>
          <Link
            href={"/catalog"}
            className="p-2 grow rounded-md hover:bg-slate-700 hover:text-white active:text-white active:bg-slate-600 duration-300"
          >
            Catalog
          </Link>
          <Link
            href={"/movies"}
            className="p-2 grow rounded-md hover:bg-slate-700 hover:text-white active:text-white active:bg-slate-600 duration-300"
          >
            Movies
          </Link>
          <Link
            href={"/shows"}
            className="p-2 grow rounded-md hover:bg-slate-700 hover:text-white active:text-white active:bg-slate-600 duration-300"
          >
            Shows
          </Link>
        </div>
        <div className="hidden md:flex max-w-6xl mx-auto justify-between items-center p-4">
          <Link
            href={"/"}
            className="font-medium text-xl duration-300 text-white hover:text-slate-200 active:text-slate-300"
          >
            Flickster
          </Link>
          <div className="flex items-center justify-center gap-4">
            <Link
              className="hover:text-slate-200 active:text-slate-300 duration-300"
              href={"/"}
            >
              Home
            </Link>
            <Link
              className="hover:text-slate-200 active:text-slate-300 duration-300"
              href={"/catalog"}
            >
              Catalog
            </Link>
            <Link
              className="hover:text-slate-200 active:text-slate-300 duration-300"
              href={"/movies"}
            >
              Movies
            </Link>
            <Link
              className="hover:text-slate-200 active:text-slate-300 duration-300"
              href={"/shows"}
            >
              TV Shows
            </Link>
          </div>
          <input
            type="text"
            className="bg-inherit rounded-md border-2 p-1 px-4 border-slate-700 hover:border-slate-500 duration-300 max-w-[16rem]"
            placeholder="Search..."
          />
        </div>
      </nav>
    </>
  );
};

export default Navbar;
