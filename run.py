"""Run from any working directory: python run.py [--port 8765]."""
import argparse

if __name__ == "__main__":
    import uvicorn
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    uvicorn.run("backend.app:app", host="127.0.0.1", port=args.port)
