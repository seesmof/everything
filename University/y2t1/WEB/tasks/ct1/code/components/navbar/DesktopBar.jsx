"use client";
import Link from "next/link";
import LinkText from "./LinkText";
import { useRouter } from "next/navigation";
import { useState } from "react";
import Input from "../Input";

const DesktopBar = ({ links, pathname }) => {
  const router = useRouter();
  const [searchQuery, setSearchQuery] = useState("");

  const handleSearchSubmit = (event) => {
    event.preventDefault();
    router.push(`/catalog?query=${searchQuery}`);
    setSearchQuery("");
  };

  return (
    <div className="hidden md:flex max-w-6xl mx-auto justify-between items-center p-4">
      <Link
        href={"/"}
        className="font-medium text-xl duration-300 text-white hover:text-indigo-400 active:text-indigo-300"
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
      <form onSubmit={handleSearchSubmit}>
        <Input
          type="text"
          placeholder="Search..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
      </form>
    </div>
  );
};

export default DesktopBar;
