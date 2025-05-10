# Create Agent Project

This project is built using Motia, a modern development framework that combines TypeScript and Python capabilities. It provides a powerful environment for creating and managing agents with AI capabilities.

## Prerequisites

- Node.js (Latest LTS version recommended)
- Python 3.8 or higher
- pnpm (Package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd create-agent
```

2. Install dependencies:
```bash
pnpm install
```

This will automatically run `motia install` as a post-install script to set up the Python environment.

## Development

To start the development server:
```bash
pnpm dev
```

For debugging mode:
```bash
pnpm dev:debug
```

## Project Structure

- `steps/` - Contains the main project steps and components
- `.motia/` - Motia framework configuration and cache
- `node_modules/` - Node.js dependencies
- `python_modules/` - Python dependencies

## Dependencies

### Node.js Dependencies
- @motiadev/core (0.1.0-beta.28)
- @motiadev/workbench (0.1.0-beta.28)
- motia (0.1.0-beta.28)
- react (^19.1.0)
- zod (^3.24.4)

### Python Dependencies
Key Python packages include:
- anthropic
- openai
- transformers
- torch
- pydantic
- python-dotenv

For a complete list of Python dependencies, see `requirements.txt`.

## Environment Variables

The project uses a `.env` file for configuration. Make sure to:
1. Create a `.env` file in the root directory
2. Add necessary environment variables
3. Never commit the `.env` file to version control

## Available Scripts

- `pnpm dev` - Start development server
- `pnpm dev:debug` - Start development server in debug mode
- `pnpm clean` - Clean build artifacts and dependencies

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

[Add your license information here] 