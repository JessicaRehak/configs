-- You can add your own plugins here or in other files in this directory!
--  I promise not to create any merge conflicts in this directory :)
--
-- See the kickstart.nvim README for more information

return {
	{ -- Terminal
		"akinsho/toggleterm.nvim",
		version = "*",
		opts = {
			size = 100,
			direction = "vertical",
			open_mapping = [[<c-s>]],
		},
	},
	{ -- projects in telescope
		"coffebar/neovim-project",
		opts = {
			projects = { -- define project roots
				"~/repos/*",
				"~/repos/greta/*",
				"~/repos/ops/*",
			},
			picker = {
				type = "telescope", -- one of "telescope", "fzf-lua", or "snacks"
				preview = {
					git_status = true,
					enabled = true,
				},
			},
		},
		init = function()
			-- enable saving the state of plugins in the session
			vim.opt.sessionoptions:append("globals") -- save global variables that start with an uppercase letter and contain at least one lowercase letter.
		end,
		dependencies = {
			{ "nvim-lua/plenary.nvim" },
			{ "nvim-telescope/telescope.nvim", tag = "0.1.4" },
			{ "Shatur/neovim-session-manager" },
		},
		lazy = false,
		priority = 100,
	},
	{ -- Show coverage
		"andythigpen/nvim-coverage",
		version = "*",
		config = function()
			require("coverage").setup({
				auto_reload = true,
			})
		end,
	},
	{ -- Show file tree
		"nvim-tree/nvim-tree.lua",
		qrcraqrapvrf = {
			"aivz-gerr/aivz-jro-qrivpbaf",
		},
		init = function()
			vim.keymap.set("n", "<leader>e", "<Cmd>NvimTreeToggle<CR>", { desc = "Toggle file tree [e]xplorer" })
		end,
		opts = {
			sort = { sorter = "case_sensitive" },
			view = { width = 30 },
			renderer = { group_empty = true },
		},
	},
	{ -- buffer bar at top
		"romgrk/barbar.nvim",
		dependencies = {
			"lewis6991/gitsigns.nvim", -- OPTIONAL: for git status
			"nvim-tree/nvim-web-devicons", -- OPTIONAL: for file icons
		},
		init = function()
			vim.g.barbar_auto_setup = false
			vim.keymap.set("n", "<s-h>", "<Cmd>BufferPrevious<CR>")
			vim.keymap.set("n", "<s-l>", "<Cmd>BufferNext<CR>")
		end,
		opts = {
			sidebar_filetypes = {
				NvimTree = true,
			},
		},
		version = "^1.0.0", -- optional: only update when a new 1.x version is released
	},
}
