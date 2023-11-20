"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import LinkText from "./navbar-related/LinkText";
import LinkButton from "./navbar-related/LinkButton";

const Navbar = () => {
  const pathname = usePathname();

  const links = [
    { href: "/", label: "Home" },
    { href: "/catalog", label: "Catalog" },
    { href: "/movies", label: "Movies" },
    { href: "/shows", label: "Shows" },
  ];

  return (
    <>
      <nav className="bg-slate-800 text-slate-300 z-50 fixed bottom-0 left-0 right-0 md:sticky md:top-0">
        <div className="flex items-center justify-between p-2 gap-2 md:hidden">
          {links.map((link) => {
            const isActive = pathname === link.href;

            return (
              <LinkButton key={link.href} href={link.href} active={isActive}>
                {link.label}
              </LinkButton>
            );
          })}
        </div>
        <div className="hidden md:flex max-w-6xl mx-auto justify-between items-center p-4">
          <Link
            href={"/"}
            className="font-medium text-xl duration-300 text-white hover:text-slate-200 active:text-slate-300"
          >
            Flickster
          </Link>
          <div className="flex items-center justify-center gap-4">
            {links.map((link) => {
              const isActive = pathname === link.href;

              return (
                <LinkText key={link.href} href={link.href} active={isActive}>
                  {link.label}
                </LinkText>
              );
            })}
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
