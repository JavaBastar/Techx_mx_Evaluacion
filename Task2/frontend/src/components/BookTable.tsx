import React from "react";

interface Book {
  id: number;
  title: string;
  price: string;
  category: string;
}

interface Props {
  books: Book[];
}

const BookTable: React.FC<Props> = ({ books }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>Título</th>
          <th>Precio</th>
          <th>Categoría</th>
        </tr>
      </thead>
      <tbody>
        {books.map((book) => (
          <tr key={book.id}>
            <td>{book.title}</td>
            <td>{book.price}</td>
            <td>{book.category}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default BookTable;
