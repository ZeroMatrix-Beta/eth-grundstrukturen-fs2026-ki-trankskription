
week1:
\begin{math-stroke}[Beispiele für Terme]
Seien $x, y$ Variablen, $F$ ein $1$-stelliges und $G$ ein $2$-stelliges Funktionssymbol.
\begin{examples}[Term-Konstruktionen]
\begin{itemize}
    \item $F x$ (entspricht $F(x)$)
    \item $G x y$ (entspricht $G(x, y)$)
    \item $G F x y$ (entspricht $G(F(x), y)$)
\end{itemize}
\end{examples}
\end{math-stroke}

\begin{math-stroke}[Bereich eines Quantors]
\begin{definition}[Bereich eines Quantors]\label[definition]{def:bereich-quantor}
Sei $\varphi$ eine $\mathcal{L}$-Formel der Form $\exists \nu \psi$ oder $\forall \nu \psi$. Dann heißt die Teilformel $\psi$ der \newterm{Bereich} (oder Wirkungsbereich) des entsprechenden Quantors.
\end{definition}
\end{math-stroke}

\emph{freie}

---

\begin{spoken-clean}[00:10:03 - 00:11:47]
Was wir heute machen --- ah, eines noch: Es gibt auch nicht-logische Axiome. Davon werden wir später noch Beispiele sehen. Das hängt von der jeweiligen Theorie ab. Wir haben gesehen, dass es eine Signatur gibt, die nicht-logische Symbole enthält, und je nach Theorie gibt es dann eben auch nicht-logische Axiome. Wir werden das in der Gruppentheorie und so weiter sehen. Diese nicht-logischen Axiome regeln dann den Gebrauch der nicht-logischen Symbole.

Später heute, in einer Stunde oder so, sehen wir noch Beispiele davon.

Gut, okay. Das ist, wo wir stehen.

Das Thema heute sind formale Beweise. Das sind eben die Regeln, wie man Sachen rein syntaktisch beweisen darf.

\inlinemetanote{Der Dozent schaltet den Projektor aus und beginnt, an der Tafel zu schreiben.}
\end{spoken-clean}

\begin{math-stroke}[Formale Beweise]
\subsection{Formale Beweise}
\end{math-stroke}

\begin{spoken-clean}[00:11:47 - 00:13:40]
Es gibt eigentlich nur zwei Schlussregeln.

Die erste Regel, die wir verwenden, um aus gegebenen Formeln eine neue Formel abzuleiten, ist der Modus Ponens. Sie bemerken ja, dass in der Logik --- weil sie aus der Antike und der Philosophie kommt --- viele Dinge lateinische Namen haben. Der berühmte Modus Ponens; abgekürzt schreiben wir oft $\text{MP}$.
