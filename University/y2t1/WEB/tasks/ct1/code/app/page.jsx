"use client";
import {
  ArrowLeftFromLine,
  ArrowRightFromLine,
  Clapperboard,
  HomeIcon,
  LayoutGrid,
  Tv,
} from "lucide-react";
import { useState } from "react";

export default function Home() {
  const [isCollapsed, setIsCollapsed] = useState(false);

  const toggleCollapsed = () => {
    setIsCollapsed(!isCollapsed);
  };

  return (
    <main className="min-h-screen bg-slate-900 text-slate-50 p-4 flex flex-col-reverse md:flex-row gap-4">
      <div className="bg-slate-800 rounded-md p-4">
        <div className="flex md:flex-col justify-between md:justify-start md:gap-4 lg:gap-6">
          <HomeIcon size={28} />
          <LayoutGrid size={28} />
          <Clapperboard size={28} />
          <Tv size={28} />
        </div>

        {isCollapsed ? (
          <button
            onClick={() => {
              toggleCollapsed();
            }}
          >
            <ArrowLeftFromLine className="self-end hidden md:block" size={28} />
          </button>
        ) : (
          <button
            onClick={() => {
              toggleCollapsed();
            }}
          >
            <ArrowRightFromLine
              className="self-end hidden md:block"
              size={28}
            />
          </button>
        )}
      </div>
      <div className="bg-slate-800 rounded-md p-4 flex-1 max-h-screen overflow-auto"></div>
    </main>
  );
}
