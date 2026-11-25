type Game<T> = {
  creator: T;
  adminList: T[];
  visits: T;
};

const strategy: Game<number> = {
  creator: 22,
  adminList: [5],
  visits: 52,
};

function doSomething<T>(param1: T, param2: number): T[] {
  const result: T[] = [];

  for (let i = 0; i < param2; i++) {
    result.push(param1);
  }

  return result;
}
