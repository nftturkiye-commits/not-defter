package com.example.fancynotebook

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.runtime.Composable
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.fancynotebook.ui.notes.AddEditNoteScreen
import com.example.fancynotebook.ui.notes.NotesScreen
import com.example.fancynotebook.ui.theme.FancyNotebookTheme
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            FancyNotebookApp()
        }
    }
}

@Composable
fun FancyNotebookApp() {
    FancyNotebookTheme {
        val navController = rememberNavController()
        NavGraph(navController = navController)
    }
}

@Composable
fun NavGraph(navController: NavHostController) {
    NavHost(navController = navController, startDestination = "notes") {
        composable("notes") {
            NotesScreen(onAddNote = { navController.navigate("edit") },
                onEditNote = { noteId -> navController.navigate("edit/$noteId") })
        }
        composable("edit") {
            AddEditNoteScreen(noteId = null, onDone = { navController.popBackStack() })
        }
        composable("edit/{noteId}") { backStackEntry ->
            val noteId = backStackEntry.arguments?.getString("noteId")?.toLongOrNull()
            AddEditNoteScreen(noteId = noteId, onDone = { navController.popBackStack() })
        }
    }
}
